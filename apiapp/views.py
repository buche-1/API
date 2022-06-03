from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import StudentSerializer, OptionSerializer, AnswerSerializer, QuestionSerializer
from .models import Student, Options, Question, Answer
# Create your views here.
class FirstView(APIView):
    def get(self, request, *args, **kwargs):
        qs = Student.objects.all()
        serializer = StudentSerializer(qs, many=True)
        return Response(serializer.data)

class ThirdView(APIView):
    def get(self, request, *args, **kwargs):
        qs = Options.objects.all()
        serializer = OptionSerializer(qs, many=True)
        return Response(serializer.data)


class SecondView(APIView):
    def get(self, request, *args, **kwargs):
        qs = Question.objects.all()
        serializer = QuestionSerializer(qs, many=True)
        return Response(serializer.data)


class FourthView(APIView):
    def get(self, request, *args, **kwargs):
        qs = Answer.objects.all()
        serializer = AnswerSerializer(qs, many=True)
        return Response(serializer.data)                

# class OptionView(APIView):
#     def get(self, request, *args, **kwargs):
#         qs = Answer.objects.all()
#         serializer = AnswerSerializer(qs, many=True)
#         return Response(serializer.data)