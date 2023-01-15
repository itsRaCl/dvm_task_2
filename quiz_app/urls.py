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
    path(
        "view-quiz-response/<int:quiz_id>/<int:question_number>",
        views.view_quiz_response,
        name="view-quiz-response",
    ),
    path("delete-quiz/<int:quiz_id>", views.delete_quiz, name="delete-quiz"),
    path("create-quiz/", views.create_quiz, name="create-quiz"),
    path(
        "add-questions/<int:quiz_id>/<int:total_questions>/<int:current_question>",
        views.add_questions,
        name="create-questions",
    ),
    path(
        "create-choice/quiz_id=<int:quiz_id>/tot_questions=<int:total_questions>/current_question=<int:current_question>/<int:total_choices>/<int:current_choice>",
        views.add_choice,
        name="create-choice",
    ),
    path("update-quiz/<int:quiz_id>", views.update_quiz, name="update-quiz"),
]
