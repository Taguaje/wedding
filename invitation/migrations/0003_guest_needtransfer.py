# Generated by Django 2.0.6 on 2019-05-29 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invitation', '0002_auto_20190529_1115'),
    ]

    operations = [
        migrations.AddField(
            model_name='guest',
            name='needTransfer',
            field=models.BooleanField(default=False),
        ),
    ]
