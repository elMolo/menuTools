# Generated by Django 3.2.5 on 2021-07-22 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0004_alter_purchase_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reciperequirement',
            name='ingredient_cost',
            field=models.FloatField(editable=False),
        ),
    ]