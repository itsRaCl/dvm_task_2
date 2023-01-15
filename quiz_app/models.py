from django.db import models
from users.models import User


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
    answer = models.CharField(max_length=100)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.TextField(max_length=100)


class QuizResponse(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    quiz_taker = models.ForeignKey(User, on_delete=models.CASCADE)


class QuestionResponse(models.Model):
    quiz = models.ForeignKey(QuizResponse, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
    status = models.CharField(max_length=10)
