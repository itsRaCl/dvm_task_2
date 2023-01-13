from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    context = {
        "quizes": [
            {
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


def view_quiz(request):
    return HttpResponse("<h1> View Quiz </h1>")


def start_quiz(request):
    return HttpResponse("<h1> Start Quiz? </h1> ")


def question_view(request):
    return HttpResponse("<h1> Question View </h1>")


def quiz_end(request):
    return HttpResponse("<h1>Quiz Ended</h1>")
