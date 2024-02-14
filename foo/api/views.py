#from django.shortcuts import render
from rest_framework import viewsets

from api.models import Examiner
from api.serializers import ExaminerSerializer


# Create your views here.
class ExaminerViewSet(viewsets.ModelViewSet):
    queryset = Examiner.objects.all()
    serializer_class = ExaminerSerializer 

'''alternative
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def getData(request):
    items = Examiner.objects.all()
    serializer = ExaminerSerializer(items, many=True) 
    return Response(serializer.data)

@api_view(['POST'])
def addExaminer(request):
    serializer = ExaminerSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

'''