# Generated by Django 4.0.4 on 2022-04-17 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('neighbour', '0009_rename_neighbourhood_id_business_neighbourhood_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='neighbourhood',
            name='date_posted',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
