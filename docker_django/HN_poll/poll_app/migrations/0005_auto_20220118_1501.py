# Generated by Django 3.2.11 on 2022-01-18 14:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('poll_app', '0004_auto_20220118_1458'),
    ]

    operations = [
		migrations.RenameModel('Voters', 'Voter')
    ]
