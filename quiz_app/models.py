from django.db import models
from django.contrib.auth.models import User


class Quiz(models.Model):
    quiz_title = models.CharField(max_length=100)
    quiz_master = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz_description = models.TextField(max_length=250)


class Question(models.Model):
    question_text = models.TextField(max_length=250)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    c_marks = models.IntegerField(default=4)
    ic_marks = models.IntegerField(default=-1)
    type = models.CharField(max_length=5)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.TextField(max_length=100)
