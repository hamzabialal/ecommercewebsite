# Generated by Django 4.2.5 on 2023-10-03 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shope', '0002_product_productimage_product_images'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='images',
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default='', upload_to='shop/images'),
        ),
        migrations.DeleteModel(
            name='ProductImage',
        ),
    ]
