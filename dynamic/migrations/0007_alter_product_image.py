# Generated by Django 4.2.6 on 2023-10-14 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dynamic', '0006_product_created_at_product_instock_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='media/images/pic2.jpg', upload_to=''),
        ),
    ]
