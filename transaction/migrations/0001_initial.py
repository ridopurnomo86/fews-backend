# Generated by Django 4.1.6 on 2023-02-17 16:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('payment_method', models.CharField(choices=[('manual', 'MANUAL'), ('card', 'CARD')], max_length=10, null=True)),
                ('total_price', models.FloatField()),
                ('shipping_price', models.FloatField()),
                ('status', models.CharField(choices=[('pending', 'PENDING'), ('success', 'SUCCESS')], max_length=10, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.user')),
                ('user_address', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.useraddress')),
            ],
        ),
    ]
