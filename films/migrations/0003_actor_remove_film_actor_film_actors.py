# Generated by Django 4.1 on 2022-11-16 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0002_remove_film_film_url_film_film_film_review_short_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=70, verbose_name='Nombre completo')),
            ],
            options={
                'verbose_name': 'Actor',
                'verbose_name_plural': 'Actores',
            },
        ),
        migrations.RemoveField(
            model_name='film',
            name='actor',
        ),
        migrations.AddField(
            model_name='film',
            name='actors',
            field=models.ManyToManyField(related_name='film_actor', to='films.actor', verbose_name='Actores'),
        ),
    ]
