# Generated by Django 3.2.5 on 2021-08-14 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_order_product_tag'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='date',
            new_name='date_created',
        ),
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
