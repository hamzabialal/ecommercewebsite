# Generated by Django 4.2.5 on 2023-10-06 08:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shope', '0015_product_major_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.RenameField(
            model_name='product',
            old_name='display_description',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='first_image',
            new_name='image',
        ),
        migrations.RemoveField(
            model_name='product',
            name='Major_category',
        ),
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.RemoveField(
            model_name='product',
            name='original_price',
        ),
        migrations.RemoveField(
            model_name='product',
            name='product_description',
        ),
        migrations.AlterField(
            model_name='product',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parent_category', to='shope.category'),
        ),
    ]
