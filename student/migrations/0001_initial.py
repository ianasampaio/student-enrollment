# Generated by Django 4.1.6 on 2023-02-08 13:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Situation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Undegraduate', 'Undegraduate'), ('Leave of absence', 'Leave of absence'), ('Graduate', 'Graduate')], max_length=20, verbose_name='Situation')),
            ],
            options={
                'verbose_name': 'Situation',
                'verbose_name_plural': 'Situations',
            },
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Subjects',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('beginSemester', models.PositiveIntegerField(verbose_name='Admission semester')),
                ('endSemester', models.PositiveIntegerField(blank=True, null=True, verbose_name='Final semester')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.situation', verbose_name='Situation')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.subject')),
            ],
            options={
                'verbose_name_plural': 'Students',
            },
        ),
    ]
