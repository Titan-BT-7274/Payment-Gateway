# Generated by Django 3.0.8 on 2020-07-31 23:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('razorpayapp', '0004_auto_20200731_2302'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='razorpayhistory',
            name='card_number',
        ),
    ]