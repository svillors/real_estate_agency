# Generated by Django 4.2.19 on 2025-02-07 12:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0012_alter_owner_name_alter_owner_owned_flats_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flat',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='flat',
            name='owners_phonenumber',
        ),
        migrations.RemoveField(
            model_name='flat',
            name='owners_pure_phonenumber',
        ),
    ]
