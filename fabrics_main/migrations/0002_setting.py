# Generated by Django 4.1.3 on 2022-12-09 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fabrics_main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('key', models.CharField(max_length=52, primary_key=True, serialize=False)),
                ('value', models.TextField()),
            ],
            options={
                'verbose_name': 'Setting',
            },
        ),
    ]
