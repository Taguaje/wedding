# Generated by Django 2.0.6 on 2019-06-03 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invitation', '0013_guest_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='guest',
            name='middleName',
            field=models.CharField(default='', max_length=100),
        ),
    ]
