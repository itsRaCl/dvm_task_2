from django import forms


class QuizConf(forms.Form):
    quiz_title = forms.CharField(max_length=100)
    quiz_description = forms.CharField(widget=forms.Textarea())
    no_of_questions = forms.IntegerField(min_value=1, initial=1)


class QuestionConf(forms.Form):
    question_text = forms.CharField(widget=forms.Textarea())
    c_marks = forms.IntegerField(initial=4)
    ic_marks = forms.IntegerField(initial=-1)
    type = forms.CharField(max_length=5)
    answer = forms.CharField(max_length=100)
    no_of_options = forms.IntegerField(
        initial=0, help_text="Leave blank for Integer and TrueFalse"
    )


class ChoiceConf(forms.Form):
    choice_text = forms.CharField(max_length=100)
