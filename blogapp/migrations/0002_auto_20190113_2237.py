# Generated by Django 2.1.4 on 2019-01-13 22:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='Price',
            new_name='description',
        ),
    ]
