# Generated by Django 4.1.3 on 2023-06-21 10:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('person_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='email',
            new_name='email_id',
        ),
        migrations.RenameField(
            model_name='person',
            old_name='phone',
            new_name='phone_number',
        ),
    ]
