# Generated by Django 2.1.7 on 2019-04-05 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LearningCenter', '0003_courses_themes'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='amount',
            field=models.IntegerField(default=0, verbose_name='Кількість академічних годин'),
        ),
        migrations.AddField(
            model_name='courses',
            name='complexity',
            field=models.IntegerField(default=0, verbose_name='Складність курсу: 1..9'),
        ),
        migrations.AddField(
            model_name='courses',
            name='description',
            field=models.TextField(default='', verbose_name='Зміст курсу'),
        ),
        migrations.AddField(
            model_name='courses',
            name='name',
            field=models.CharField(default='', max_length=40),
        ),
        migrations.AddField(
            model_name='courses',
            name='pages',
            field=models.IntegerField(default=0, verbose_name='Кількість сторінок інструкцій'),
        ),
        migrations.AddField(
            model_name='themes',
            name='amount',
            field=models.IntegerField(default=0, verbose_name='Кількість академічних годин'),
        ),
        migrations.AddField(
            model_name='themes',
            name='complexity',
            field=models.IntegerField(default=0, verbose_name='Складність теми: 1..9'),
        ),
        migrations.AddField(
            model_name='themes',
            name='description',
            field=models.TextField(default='', verbose_name='Зміст теми'),
        ),
        migrations.AddField(
            model_name='themes',
            name='name',
            field=models.CharField(default='', max_length=80),
        ),
        migrations.AddField(
            model_name='themes',
            name='pages',
            field=models.IntegerField(default=0, verbose_name='Кількість сторінок інструкцій'),
        ),
    ]
