from django import forms
from .models import Question, Quiz
from django.utils.translation import gettext_lazy as _

QUESTION_TYPES = [
    ("SCQ", "SCQ"),
    ("MCQ", "MCQ"),
    ("INT", "Integer"),
    ("TF", "True/False"),
]


class QuizConf(forms.ModelForm):
    no_of_questions = forms.IntegerField(min_value=1, initial=1)

    class Meta:
        model = Quiz
        fields = ["quiz_title", "quiz_description", "no_of_questions", "quiz_password"]
        help_texts = {
            "quiz_password": _("Enter password if you want to have a password"),
        }


class QuestionConf(forms.ModelForm):
    no_of_options = forms.IntegerField(
        initial=0, help_text="Leave as is for Integer and TrueFalse"
    )

    class Meta:
        model = Question
        fields = [
            "question_text",
            "c_marks",
            "ic_marks",
            "type",
            "answer",
            "no_of_options",
        ]
        widgets = {"type": forms.RadioSelect(choices=QUESTION_TYPES)}


class ChoiceConf(forms.Form):
    choice_text = forms.CharField(max_length=100)


class UpdateQuestion(forms.ModelForm):
    class Meta:
        model = Question
        fields = ["question_text", "c_marks", "ic_marks", "answer"]


class UpdateChoice(forms.Form):
    choice_text = forms.CharField(max_length=100)
