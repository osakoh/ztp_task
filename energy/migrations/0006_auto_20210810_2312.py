# Generated by Django 3.2.6 on 2021-08-10 22:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('energy', '0005_auto_20210810_2311'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='consumption',
            name='cost',
        ),
        migrations.RemoveField(
            model_name='consumption',
            name='energy_consumed',
        ),
        migrations.RemoveField(
            model_name='consumption',
            name='total',
        ),
    ]