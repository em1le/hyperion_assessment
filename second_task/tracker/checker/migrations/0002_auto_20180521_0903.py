# Generated by Django 2.0.5 on 2018-05-21 09:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checker', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='filedata',
            old_name='date',
            new_name='modification_date',
        ),
    ]
