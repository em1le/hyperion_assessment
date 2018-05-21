# Generated by Django 2.0.5 on 2018-05-20 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FileData',
            fields=[
                ('file_id', models.CharField(max_length=64, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('date', models.DateTimeField()),
                ('occurence', models.PositiveIntegerField(default=1)),
            ],
        ),
    ]
