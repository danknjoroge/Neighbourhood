# Generated by Django 4.0.4 on 2022-04-17 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('neighbour', '0007_rename_neighbourhood_business_neighbourhood_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='default.png', upload_to=''),
        ),
    ]