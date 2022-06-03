from rest_framework import serializers
from .models import Student, Question, Options, Answer

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = (
            'name', 'age'
        )

class QuestionSerializer(serializers.ModelSerializer):
       class Meta:
        model = Question
        fields = '__all__'


class OptionSerializer(serializers.ModelSerializer):
       class Meta:
        model = Options
        
        fields = (
            'question', 'A','B','C','D'
        )    

class AnswerSerializer(serializers.ModelSerializer):
       class Meta:
        model = Answer
        fields = (
            'question','answer'
        )    