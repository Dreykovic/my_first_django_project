# Generated by Django 4.2.7 on 2023-11-26 13:30

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Eleve',
            fields=[
                ('nom', models.CharField(max_length=50)),
                ('prenom', models.CharField(max_length=50)),
                ('sexe', models.CharField(choices=[('M', 'Masculin'), ('F', 'Feminin')], max_length=20)),
                ('date_naissance', models.DateField()),
                ('id', models.CharField(max_length=55, primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': 'Eleve',
                'verbose_name_plural': 'Eleves',
            },
        ),
        migrations.CreateModel(
            name='Enseignant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('prenom', models.CharField(max_length=50)),
                ('sexe', models.CharField(choices=[('M', 'Masculin'), ('F', 'Feminin')], max_length=20)),
                ('date_naissance', models.DateField()),
            ],
            options={
                'verbose_name': 'Enseignant',
                'verbose_name_plural': 'Enseignants',
            },
        ),
        migrations.CreateModel(
            name='Matiere',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50, unique=True)),
                ('enseignant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notes.enseignant')),
            ],
            options={
                'verbose_name': 'Matiere',
                'verbose_name_plural': 'Matieres',
            },
        ),
        migrations.CreateModel(
            name='Niveau',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=2, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valeur', models.FloatField(null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(20)])),
                ('eleve', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notes.eleve')),
                ('matiere', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notes.matiere')),
            ],
            options={
                'verbose_name': 'Note',
                'verbose_name_plural': 'Notes',
            },
        ),
        migrations.AddField(
            model_name='matiere',
            name='niveaus',
            field=models.ManyToManyField(to='notes.niveau'),
        ),
        migrations.AddField(
            model_name='eleve',
            name='niveau',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notes.niveau'),
        ),
    ]