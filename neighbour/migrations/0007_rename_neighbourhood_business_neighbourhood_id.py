# Generated by Django 4.0.4 on 2022-04-17 20:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('neighbour', '0006_rename_neighbourhood_userprofile_neighbourhood_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='business',
            old_name='neighbourhood',
            new_name='neighbourhood_id',
        ),
    ]
