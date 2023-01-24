from .models import Quiz


def reset_responses(quiz_id):
    quiz = Quiz.objects.get(pk=quiz_id)

    for i in quiz.quizresponse_set.all():
        i.delete()


def calculate_marks(quiz_response):
    question_responses = list(quiz_response.questionresponse_set.all()) + list(
        quiz_response.mcqresponse_set.all()
    )
    for i in question_responses:
        if i.status == "C":
            quiz_response.marks_secured += i.question.c_marks
        elif i.status == "IC":
            quiz_response.marks_secured += i.question.ic_marks
        elif i.status == "UA":
            quiz_response.marks_secured += 0
        elif i.status == "PC":
            partial_marks = i.question.c_marks / len(list(i.question.choice_set.all()))
            quiz_response.marks_secured += partial_marks * len(
                list(i.mcqchoiceresponse_set.all())
            )
    quiz_response.save()
