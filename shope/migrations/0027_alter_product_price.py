# Generated by Django 4.2.5 on 2023-10-09 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shope', '0026_alter_product_arrival'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
