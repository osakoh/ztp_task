# Generated by Django 3.2.6 on 2021-08-11 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('energy', '0007_consumption_cost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consumption',
            name='cost',
            field=models.FloatField(blank=True, default='cal_cost()', null=True),
        ),
    ]
