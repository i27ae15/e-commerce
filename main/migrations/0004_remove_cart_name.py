# Generated by Django 4.0.2 on 2022-02-08 07:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='name',
        ),
    ]
