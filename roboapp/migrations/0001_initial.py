# Generated by Django 2.1 on 2018-08-10 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='mqttbroker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mqttbroker', models.CharField(help_text='Enter field documentation', max_length=20)),
                ('mqtthost', models.CharField(help_text='Enter field documentation', max_length=20)),
                ('mqttport', models.CharField(help_text='Enter field documentation', max_length=20)),
                ('mqttrobot', models.CharField(default='', help_text='Enter field documentation', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='robot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='', help_text='Enter field documentation', max_length=20)),
                ('password', models.CharField(default='', help_text='Enter field documentation', max_length=20)),
            ],
        ),
    ]
