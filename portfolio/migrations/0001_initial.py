# Generated by Django 5.1.1 on 2025-02-02 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ValetCars',
            fields=[
                ('ticketNum', models.IntegerField(primary_key=True, serialize=False)),
                ('lastName', models.CharField(max_length=50)),
                ('departureDate', models.DateTimeField()),
                ('carMake', models.CharField(max_length=50)),
                ('carModel', models.CharField(max_length=50)),
                ('carColor', models.CharField(max_length=50)),
            ],
        ),
    ]
