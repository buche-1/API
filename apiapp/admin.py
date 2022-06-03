from django.contrib import admin
from .models import Student, Question, Options, Answer
# Register your models here.
admin.site.register(Student)
admin.site.register(Options)
admin.site.register(Answer)
admin.site.register(Question)