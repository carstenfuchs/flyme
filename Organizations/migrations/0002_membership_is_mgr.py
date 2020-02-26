# Generated by Django 3.0.2 on 2020-02-26 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Organizations', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='membership',
            name='is_mgr',
            field=models.BooleanField(default=False, help_text='Is the member given management access to the organization?'),
        ),
    ]
