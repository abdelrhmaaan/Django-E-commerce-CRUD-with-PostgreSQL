# Generated by Django 4.2.6 on 2023-10-13 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dynamic', '0004_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='images/default.jpg', upload_to='images/'),
        ),
    ]
