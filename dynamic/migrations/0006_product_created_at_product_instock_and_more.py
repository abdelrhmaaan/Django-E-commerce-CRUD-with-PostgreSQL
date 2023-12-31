# Generated by Django 4.2.6 on 2023-10-14 12:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('dynamic', '0005_alter_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='inStock',
            field=models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], default='yes', max_length=3),
        ),
        migrations.AddField(
            model_name='product',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='media/images/pic2.jpg', upload_to='images/'),
        ),
    ]
