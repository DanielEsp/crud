# Generated by Django 3.2.9 on 2021-11-24 05:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0006_alter_user_mail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
    ]
