# Generated by Django 4.2.5 on 2023-10-09 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shope', '0029_alter_product_discount_percentage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=1, max_digits=10),
        ),
    ]
