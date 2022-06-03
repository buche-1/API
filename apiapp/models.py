from django.db import models


# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return self.name


class Question(models.Model):
    question = models.CharField(max_length=100)

    def __str__(self):
        return self.question


class Options(models.Model):
    question = models.ForeignKey(Question, on_delete= models.CASCADE)
    A =  models.CharField(max_length=100)
    B =  models.CharField(max_length=100)
    C =  models.CharField(max_length=100)
    D =  models.CharField(max_length=100) 

    def __str__(self):
        return self.A


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete= models.CASCADE)
    answer = models.CharField(max_length=100)
    
    def __str__(self):
        return self.answer