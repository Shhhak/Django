# Generated by Django 3.2.3 on 2021-05-14 17:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='pub_data',
            new_name='pub_date',
        ),
    ]
