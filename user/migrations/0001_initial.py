# Generated by Django 4.1.6 on 2023-02-17 16:16

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('full_name', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=255, validators=[django.core.validators.MinLengthValidator(8)])),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('is_email_verified', models.IntegerField(default=0)),
                ('gender', models.CharField(choices=[('men', 'Men'), ('women', 'Women')], max_length=5, null=True)),
                ('birth_date', models.DateTimeField(blank=True, null=True)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('address_name', models.CharField(max_length=200)),
                ('country', models.CharField(max_length=100)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
        ),
    ]
