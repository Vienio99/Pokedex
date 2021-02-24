# Generated by Django 3.1.6 on 2021-02-24 20:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pokedex', '0005_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='pokemon',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='pokedex.pokemon'),
        ),
    ]
