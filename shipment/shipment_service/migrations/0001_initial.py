# Generated by Django 4.0.1 on 2024-05-06 12:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carriers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.FloatField()),
                ('address', models.CharField(max_length=200)),
                ('is_active', models.BooleanField(default=True)),
                ('mobile', models.CharField(max_length=11)),
                ('email', models.CharField(max_length=50)),
                ('des', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='ShipmentInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=50)),
                ('lname', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('mobile', models.CharField(max_length=12)),
                ('address', models.CharField(max_length=200)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('coefficient', models.FloatField()),
                ('is_active', models.BooleanField(default=True)),
                ('des', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Shipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.IntegerField()),
                ('shipment_status', models.CharField(max_length=20)),
                ('payment_status', models.CharField(max_length=15)),
                ('carrier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shipment_service.carriers')),
                ('shipment_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shipment_service.shipmentinfo')),
                ('transaction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shipment_service.transaction')),
            ],
        ),
    ]
