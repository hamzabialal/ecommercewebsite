# Generated by Django 4.2.5 on 2023-10-09 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shope', '0024_productdescription_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='arrival',
            field=models.BooleanField(default=True),
        ),
    ]
