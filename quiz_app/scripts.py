from .models import Quiz


def reset_responses(quiz_id):
    quiz = Quiz.objects.get(pk=quiz_id)

    for i in quiz.quizresponse_set.all():
        i.delete()
