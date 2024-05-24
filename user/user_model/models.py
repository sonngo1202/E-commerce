from django.db import models

class Fullname(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

class Address(models.Model):
    city = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    commune = models.CharField(max_length=50)
    street = models.CharField(max_length=50)

class Account(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def set_password(self, raw_password):
        self.password = raw_password

class Contact(models.Model):
    email = models.CharField(max_length=50)
    mobile = models.CharField(max_length=12)

class User(models.Model):
    id = models.CharField(max_length=7, primary_key=True)
    dob = models.DateField()
    is_active = models.BooleanField(default=True)
    position = models.IntegerField()
    fullname = models.ForeignKey(Fullname, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)