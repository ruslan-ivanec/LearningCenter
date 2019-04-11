from django.db import models

class Center(models.Model):
    name = models.CharField(max_length=60)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    eMail = models.CharField(max_length=40)

class Levels(models.Model):
    name = models.CharField(max_length=20)

class Types(models.Model):
    name = models.CharField(max_length=20)

class Teachers(models.Model):
    name = models.CharField(max_length=20)
    degree = models.CharField(max_length=30)
    phone = models.CharField(max_length=20)
    eMail = models.CharField(max_length=30)

class Disciplines(models.Model):
    name = models.CharField(max_length=40)

class Courses(models.Model):
    name = models.CharField(max_length=40,default='')
    disciplineId = models.ForeignKey(Disciplines, on_delete=models.CASCADE)
    typeId = models.ForeignKey(Types, on_delete=models.CASCADE)
    levelId = models.ForeignKey(Levels, on_delete=models.CASCADE)
    teacherId = models.ForeignKey(Teachers, on_delete=models.CASCADE,blank=True)
    amount = models.IntegerField('Кількість академічних годин',default=0,blank=True)
    pages = models.IntegerField('Кількість сторінок інструкцій',default=0,blank=True)
    complexity = models.IntegerField('Складність курсу: 1..9',default=0)
    description = models.TextField('Зміст курсу',default='')

class Themes(models.Model):
    name = models.CharField(max_length=80,default='')
    courseId = models.ForeignKey(Courses, on_delete=models.CASCADE)
    amount = models.IntegerField('Кількість академічних годин',default=0,blank=True)
    pages = models.IntegerField('Кількість сторінок інструкцій',default=0,blank=True)
    complexity = models.IntegerField('Складність теми: 1..9',default=0)
    description = models.TextField('Зміст теми',default='',blank=True)
