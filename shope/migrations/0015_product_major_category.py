# Generated by Django 4.2.5 on 2023-10-06 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shope', '0014_alter_product_parent'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='Major_category',
            field=models.CharField(default='', max_length=255),
        ),
    ]