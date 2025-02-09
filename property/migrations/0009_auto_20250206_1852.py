# Generated by Django 4.2.19 on 2025-02-06 15:52

from django.db import migrations
from phonenumbers import parse, is_valid_number


def set_pure_phone_numbeer(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    for flat in Flat.objects.all():
        if is_valid_number(parse(flat.owners_phonenumber, 'RU')):
            phone_number = flat.owners_phonenumber
            flat.owners_pure_phonenumber = f'+7{parse(phone_number, "RU").national_number}'
        else:
            flat.owners_pure_phonenumber = ''
        flat.save()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0008_alter_flat_liked'),
    ]

    operations = [
        migrations.RunPython(set_pure_phone_numbeer),
    ]
