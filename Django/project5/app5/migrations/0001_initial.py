# Generated by Django 4.2.2 on 2025-06-17 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fname', models.CharField(max_length=30)),
                ('Lname', models.CharField(max_length=30)),
                ('Marks', models.FloatField()),
                ('Location', models.CharField(max_length=20)),
            ],
        ),
    ]
