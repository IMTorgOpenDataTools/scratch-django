#from django.shortcuts import render
from rest_framework import viewsets

from api.models import Examiner
from api.serializers import ExaminerSerializer


# Create your views here.
class ExaminerViewSet(viewsets.ModelViewSet):
    queryset = Examiner.objects.all()
    serializer_class = ExaminerSerializer 