# Generated by Django 2.0.5 on 2019-06-06 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invitation', '0016_guest_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guest',
            name='order',
            field=models.IntegerField(blank=True, default=9999),
        ),
    ]
