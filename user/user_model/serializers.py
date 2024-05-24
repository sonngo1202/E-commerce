from rest_framework import serializers
from .models import Contact, User, Fullname, Address, Account

class FullnameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fullname
        fields = "__all__"

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = "__all__"

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = "__all__"

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
    fullname = FullnameSerializer()
    address = AddressSerializer()
    account = AccountSerializer()
    contact = ContactSerializer()

    class Meta:
        model = User
        fields = "__all__"
    
    def create(self, validated_data):
        fullname_data = validated_data.pop('fullname')
        address_data = validated_data.pop('address')
        account_data = validated_data.pop('account')
        contact_data = validated_data.pop('contact')

        fullname_instance = Fullname.objects.create(**fullname_data)
        address_instance = Address.objects.create(**address_data)
        account_instance = Account.objects.create(**account_data)
        contact_instance = Contact.objects.create(**contact_data)

        user = User.objects.create(fullname=fullname_instance, address=address_instance, account=account_instance, contact=contact_instance, **validated_data)
        return user


    def destroy(self, instance):
        instance.is_active = False
        instance.save()
        return instance

class UserUpdateSerializer(serializers.ModelSerializer):
    fullname = FullnameSerializer()
    address = AddressSerializer()
    contact = ContactSerializer()

    class Meta:
        model = User
        fields = ['fullname', 'address', 'contact', 'dob']

    def update(self, instance, validated_data):
        instance.dob = validated_data.get('dob', instance.dob)
        instance.save()

        fullname_data = validated_data.pop('fullname', None)
        address_data = validated_data.pop('address', None)
        contact_data = validated_data.pop('contact', None)

        if fullname_data:
            fullname_serializer = FullnameSerializer(instance.fullname, data=fullname_data)
            if fullname_serializer.is_valid():
                fullname_serializer.save()

        if address_data:
            address_serializer = AddressSerializer(instance.address, data=address_data)
            if address_serializer.is_valid():
                address_serializer.save()

        if contact_data:
            contact_serializer = ContactSerializer(instance.contact, data=contact_data)
            if contact_serializer.is_valid():
                contact_serializer.save()

        return instance


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField()
    new_password = serializers.CharField()

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        username = data.get('username', None)
        password = data.get('password', None)
        account = Account.objects.filter(username=username).first()
        if account and account.password == password:
            return User.objects.filter(account=account, is_active=True).first()
        else:
            raise serializers.ValidationError('Invalid username or password.')

