# Generated by Django 4.2.5 on 2023-10-12 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shope', '0031_alter_product_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShippingAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=70)),
                ('last_name', models.CharField(max_length=70)),
                ('company_name', models.CharField(blank=True, max_length=67)),
                ('area_code', models.CharField(max_length=5)),
                ('primary_field', models.CharField(max_length=20)),
                ('street_address', models.CharField(max_length=300)),
                ('zip_code', models.CharField(max_length=13)),
                ('business_address', models.BooleanField()),
            ],
        ),
    ]
