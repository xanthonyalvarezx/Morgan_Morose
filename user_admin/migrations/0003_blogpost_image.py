# Generated by Django 3.2.7 on 2021-09-14 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_admin', '0002_images'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='image',
            field=models.FileField(default=1, upload_to='images/'),
            preserve_default=False,
        ),
    ]
