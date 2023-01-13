from django.shortcuts import render
from django.http import HttpResponse
from .models import Quiz, Question, Choice

# Create your views here.
def home(request):
    context = {
        "quizes": [
            {
                "quiz_id": 1,
                "quiz_title": "Quiz 1",
                "quiz_master": "Quiz Master 1",
                "quiz_description": "This is the first quiz by quiz master 1",
                "c_marks": 4,
                "ic_marks": -1,
                "other_marks": "-",
            },
        ]
    }
    return render(request, "quiz_app/home.html", context=context)


def view_quiz(request, quiz_id):
    # quiz = Quiz.objects.get(pk=quiz_id)
    # context = {
    #     "quiz_id": quiz.id,
    #     "quiz_title": quiz.quiz_title,
    #     "quiz_description": quiz.quiz_description,
    #     "quiz_master": quiz.quiz_master,
    # }
    context = {
        "quiz_id": 1,
        "quiz_title": "Quiz 1",
        "quiz_master": "Quiz Master 1",
        "quiz_description": "This is the first quiz by quiz master 1",
        "c_marks": 4,
        "ic_marks": -1,
        "other_marks": "-",
    }
    return render(request, "quiz_app/start_quiz.html", context=context)


def start_quiz(request):
    return HttpResponse("<h1> Start Quiz? </h1> ")


def question_view(request, quiz_id, question_no):
    return HttpResponse(f"<h1> Question View {question_no}</h1>")


def quiz_end(request):
    return HttpResponse("<h1>Quiz Ended</h1>")
