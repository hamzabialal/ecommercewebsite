# Generated by Django 4.2.5 on 2023-10-17 10:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shope', '0037_wishlist_cart'),
    ]

    operations = [
        migrations.CreateModel(
            name='CheckoutCart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('total', models.IntegerField(blank=True, default=0, null=True)),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shope.product')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CreateCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('card_number', models.IntegerField()),
                ('exp_year', models.CharField(max_length=30)),
                ('exp_month', models.CharField(max_length=30)),
                ('CSV', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='StripePaymentIntentId',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_intent_id', models.CharField(blank=True, max_length=255, null=True)),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shope.product')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='CardInformation',
        ),
        migrations.RemoveField(
            model_name='shippingaddress',
            name='business_address',
        ),
        migrations.RemoveField(
            model_name='shippingaddress',
            name='company_name',
        ),
        migrations.RemoveField(
            model_name='shippingaddress',
            name='primary_field',
        ),
        migrations.RemoveField(
            model_name='shippingaddress',
            name='street_address',
        ),
        migrations.AddField(
            model_name='shippingaddress',
            name='address',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='shippingaddress',
            name='busines_address',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='shippingaddress',
            name='comp_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='shippingaddress',
            name='phone',
            field=models.CharField(default='', max_length=15),
        ),
        migrations.AddField(
            model_name='shippingaddress',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shope.product'),
        ),
        migrations.AddField(
            model_name='shippingaddress',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='shippingaddress',
            name='area_code',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='shippingaddress',
            name='first_name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='shippingaddress',
            name='last_name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='shippingaddress',
            name='zip_code',
            field=models.CharField(max_length=20),
        ),
    ]