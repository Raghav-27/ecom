# Generated by Django 3.0.5 on 2024-10-13 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_auto_20241013_1703'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='imageq',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='product',
            name='imagev',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='product',
            name='imagew',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
