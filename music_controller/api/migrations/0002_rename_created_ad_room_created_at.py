# Generated by Django 4.2.3 on 2023-07-12 17:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='created_ad',
            new_name='created_at',
        ),
    ]
