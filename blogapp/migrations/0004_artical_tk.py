# Generated by Django 2.1.4 on 2019-01-18 11:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0003_auto_20190118_1059'),
    ]

    operations = [
        migrations.AddField(
            model_name='artical',
            name='tk',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]