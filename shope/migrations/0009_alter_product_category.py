# Generated by Django 4.2.5 on 2023-10-04 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shope', '0008_product_first_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
