# Generated by Django 3.1 on 2020-08-25 17:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MovieInfo', '0005_auto_20200825_1710'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movieinfo',
            old_name='moive_desc',
            new_name='movie_desc',
        ),
    ]
