# Generated by Django 3.2.5 on 2021-08-14 14:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20210814_1553'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='date_created',
            new_name='date',
        ),
    ]
