# Generated by Django 2.2.2 on 2019-06-22 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ParamConfig',
            fields=[
                ('key', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('value', models.CharField(max_length=100)),
                ('remark', models.CharField(max_length=100)),
                ('created', models.DateTimeField(verbose_name='config created')),
            ],
        ),
    ]