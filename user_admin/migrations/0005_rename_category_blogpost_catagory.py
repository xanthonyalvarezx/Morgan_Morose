# Generated by Django 3.2.7 on 2021-09-15 16:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_admin', '0004_blogpost_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogpost',
            old_name='category',
            new_name='catagory',
        ),
    ]
