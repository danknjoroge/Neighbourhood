# Generated by Django 4.0.4 on 2022-04-18 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('neighbour', '0013_business_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='bio',
            field=models.TextField(default=''),
        ),
    ]
