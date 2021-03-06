# Generated by Django 3.2.5 on 2021-07-27 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0006_remove_reciperequirement_ingredient_cost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='unitPrice',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='price',
            field=models.DecimalField(decimal_places=2, default=11.5, max_digits=10),
        ),
    ]
