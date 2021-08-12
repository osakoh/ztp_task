# Generated by Django 3.2.6 on 2021-08-10 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('energy', '0003_alter_consumption_second'),
    ]

    operations = [
        migrations.AddField(
            model_name='consumption',
            name='cost',
            field=models.FloatField(null=True, verbose_name='Cost'),
        ),
        migrations.AddField(
            model_name='consumption',
            name='energy_consumed',
            field=models.FloatField(null=True, verbose_name='Energy Consumption'),
        ),
        migrations.AddField(
            model_name='consumption',
            name='total',
            field=models.FloatField(null=True, verbose_name='Total Energy cost'),
        ),
    ]