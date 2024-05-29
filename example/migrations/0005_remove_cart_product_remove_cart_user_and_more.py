# Generated by Django 4.1.3 on 2024-05-29 11:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('example', '0004_buyeruser_cart_categories_checkoutinfo_customuser_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='product',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='user',
        ),
        migrations.RemoveField(
            model_name='checkoutinfo',
            name='cart',
        ),
        migrations.RemoveField(
            model_name='checkoutinfo',
            name='user',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='user_m',
        ),
        migrations.RemoveField(
            model_name='frameruser',
            name='customuser',
        ),
        migrations.RemoveField(
            model_name='product',
            name='categories',
        ),
        migrations.RemoveField(
            model_name='product',
            name='framer_user',
        ),
        migrations.RemoveField(
            model_name='productimages',
            name='product',
        ),
        migrations.RemoveField(
            model_name='shippinginfo',
            name='checkout_info',
        ),
        migrations.DeleteModel(
            name='BuyerUser',
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
        migrations.DeleteModel(
            name='Categories',
        ),
        migrations.DeleteModel(
            name='CheckOutInfo',
        ),
        migrations.DeleteModel(
            name='CustomUser',
        ),
        migrations.DeleteModel(
            name='FramerUser',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.DeleteModel(
            name='ProductImages',
        ),
        migrations.DeleteModel(
            name='ShippingInfo',
        ),
    ]