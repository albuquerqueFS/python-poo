# Generated by Django 4.1 on 2022-08-25 18:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('office', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patient',
            old_name='fist_name',
            new_name='first_name',
        ),
    ]
