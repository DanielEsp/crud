# Generated by Django 3.2.9 on 2021-11-23 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shipment',
            fields=[
                ('id', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('owner', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('DF', 'Draft'), ('PD', 'Pending'), ('DV', 'Delivered')], default='DF', max_length=2)),
            ],
        ),
    ]
