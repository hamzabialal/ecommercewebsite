# Generated by Django 4.2.5 on 2023-10-13 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shope', '0032_shippingaddress'),
    ]

    operations = [
        migrations.CreateModel(
            name='CardInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cardholder_name', models.CharField(max_length=200)),
                ('card_number', models.CharField(max_length=16)),
                ('payment_types', models.CharField(max_length=200)),
                ('expiration_data', models.CharField(max_length=200)),
                ('csc', models.CharField(max_length=3)),
            ],
        ),
    ]
