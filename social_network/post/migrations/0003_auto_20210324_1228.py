# Generated by Django 3.1.7 on 2021-03-24 12:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_post_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='likes',
            new_name='like',
        ),
    ]
