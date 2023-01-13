from django.urls import path
from . import views

app_name = "quiz"
urlpatterns = [
    path("", views.home, name="quiz-home"),
    path("view/<int:quiz_id>/", views.view_quiz, name="view-quiz"),
    path(
        "take/<int:quiz_id>/<int:question_no>",
        views.question_view,
        name="view-question",
    ),
]
