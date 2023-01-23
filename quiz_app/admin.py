from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(QuizResponse)
admin.site.register(QuestionResponse)
admin.site.register(mcqResponse)
admin.site.register(mcqChoiceResponse)
