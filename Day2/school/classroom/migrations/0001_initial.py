# Generated by Django 5.1.6 on 2025-03-03 20:50

import django.db.models.aggregates
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Classroom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('year', models.IntegerField()),
                ('teacher', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('age', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('number_of_classrooms', models.IntegerField(verbose_name=django.db.models.aggregates.Count('classrooms'))),
                ('address', models.TextField()),
                ('classrooms', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='schools', to='classroom.classroom')),
            ],
        ),
        migrations.AddField(
            model_name='classroom',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='classrooms', to='classroom.student'),
        ),
        migrations.AddField(
            model_name='classroom',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='classrooms', to='classroom.subject'),
        ),
    ]
