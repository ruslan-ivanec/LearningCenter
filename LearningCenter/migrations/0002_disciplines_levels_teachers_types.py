# Generated by Django 2.1.7 on 2019-04-05 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LearningCenter', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Disciplines',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Levels',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Teachers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('degree', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=20)),
                ('eMail', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Types',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
    ]