# Generated by Django 4.1 on 2022-11-19 21:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0003_actor_remove_film_actor_film_actors'),
    ]

    operations = [
        migrations.RenameField(
            model_name='film',
            old_name='film',
            new_name='movie',
        ),
    ]
