# Generated by Django 2.0 on 2020-06-13 19:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0002_auto_20200613_1937'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registration',
            old_name='qualifications',
            new_name='qualification',
        ),
    ]