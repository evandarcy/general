# Generated by Django 2.1 on 2018-08-11 10:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('roboapp', '0007_auto_20180811_0959'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='authors',
        ),
        migrations.AddField(
            model_name='robot',
            name='broker',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='roboapp.mqttbroker'),
        ),
    ]
