# Generated by Django 3.2.11 on 2022-01-18 13:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('poll_app', '0003_voters'),
    ]

    operations = [
		migrations.RenameModel('Nominee', 'Candidate')
    ]