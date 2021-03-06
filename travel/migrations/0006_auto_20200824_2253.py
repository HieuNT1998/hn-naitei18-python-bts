# Generated by Django 3.0.8 on 2020-08-24 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0005_merge_20200824_0927'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='url',
            field=models.ImageField(upload_to='images/tours/1'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(default='media/images/avatar/userde.JPG', upload_to='media/images/avatar'),
        ),
    ]
