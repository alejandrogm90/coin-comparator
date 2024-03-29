# Generated by Django 4.1.7 on 2023-05-24 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='coin_day',
            fields=[
                ('id', models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='id')),
                ('date_part', models.CharField(max_length=10, verbose_name='date_part')),
                ('name', models.CharField(max_length=10, verbose_name='name')),
                ('value', models.FloatField()),
            ],
        ),
    ]
