# Generated by Django 4.1.3 on 2024-05-29 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('example', '0010_alter_product_image_mycart'),
    ]

    operations = [
        migrations.AddField(
            model_name='mycart',
            name='status',
            field=models.CharField(choices=[('cart', 'cart'), ('purchased', 'purchased')], default='cart', max_length=15),
        ),
    ]