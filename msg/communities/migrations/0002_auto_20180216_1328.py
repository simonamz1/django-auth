# Generated by Django 2.0.2 on 2018-02-16 13:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('communities', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='communitymember',
            options={'permissions': (('ban_member', 'Can ban members'),)},
        ),
    ]
