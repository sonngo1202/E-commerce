# Generated by Django 4.0.1 on 2024-05-12 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=7)),
                ('product_id', models.CharField(max_length=7)),
                ('comment', models.CharField(max_length=250)),
                ('rate', models.IntegerField()),
                ('date_added', models.DateField(auto_now_add=True)),
            ],
        ),
    ]