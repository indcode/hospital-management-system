# Generated by Django 2.0 on 2020-06-23 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0027_remove_registrationp_medical_history'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='payment',
            field=models.CharField(default='no', max_length=150),
        ),
    ]
