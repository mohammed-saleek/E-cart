# Generated by Django 4.0.1 on 2022-07-11 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cartapp', '0003_remove_order_transaction_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shippingaddress',
            old_name='city',
            new_name='country',
        ),
        migrations.AddField(
            model_name='shippingaddress',
            name='email',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='shippingaddress',
            name='first_name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='shippingaddress',
            name='last_name',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
