# Generated by Django 4.2.2 on 2025-06-20 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app7', '0002_alter_vehicleparking_parking_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicleparking',
            name='Parking_Date',
            field=models.DateField(),
        ),
    ]
