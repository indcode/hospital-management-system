# Generated by Django 2.0 on 2020-06-20 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0014_auto_20200620_1656'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notification',
            name='doct_key',
        ),
        migrations.RemoveField(
            model_name='notification',
            name='patient',
        ),
        migrations.AddField(
            model_name='notification',
            name='appntmnt',
            field=models.ForeignKey(null=True, on_delete='DO_NOTHING', to='patient.appointment'),
        ),
    ]