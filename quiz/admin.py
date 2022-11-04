from django.contrib import admin
from .models import *

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display =['course', 'marks', 'question', 'option1', 'option2', 'option3', 'option4', 'answer']
