# Generated by Django 4.2.5 on 2023-10-07 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shope', '0021_remove_productdescription_camera_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ParentCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]
