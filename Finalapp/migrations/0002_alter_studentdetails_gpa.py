# Generated by Django 3.2.2 on 2021-05-10 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Finalapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentdetails',
            name='gpa',
            field=models.DecimalField(decimal_places=2, max_digits=4),
        ),
    ]
