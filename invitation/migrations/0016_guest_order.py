# Generated by Django 2.0.5 on 2019-06-06 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invitation', '0015_auto_20190603_2121'),
    ]

    operations = [
        migrations.AddField(
            model_name='guest',
            name='order',
            field=models.ImageField(blank=True, default=9999, upload_to=''),
        ),
    ]
