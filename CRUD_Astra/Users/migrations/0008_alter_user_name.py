# Generated by Django 3.2.9 on 2021-11-25 04:02

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0007_alter_user_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=100, validators=[django.core.validators.RegexValidator("^[a-zA-Z]+(([\\',. -][a-zA-Z ])?[a-zA-Z]*)*$", 'Only valid names accepted')]),
        ),
    ]
