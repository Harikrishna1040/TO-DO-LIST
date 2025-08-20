from django.shortcuts import render
from django.http import HttpResponse
from .models import todotask
from rest_framework.decorators  import api_view
from .serializers import taskserializer
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK,HTTP_400_BAD_REQUEST
# Create your views here.

def display(request):
    if request.method=='GET':
        return HttpResponse('go ahead')
@api_view(['GET','POST'])
def gettasks(request):
    if request.method=='GET':
        taskobj=todotask.objects.all()
        serializer_obj=taskserializer(taskobj,many=True)
        return Response(serializer_obj.data)
    if request.method=='POST':
        serializer_obj=taskserializer(data=request.data)
        if serializer_obj.is_valid()==True:
            serializer_obj.save()
            return Response(status=HTTP_200_OK)
        else:
            return Response(status=HTTP_400_BAD_REQUEST)

@api_view(['PUT','GET','DELETE'])
def modifytask(request,pk):
    def get_pk(pk):
        try:
            task=todotask.objects.get(pk=pk)
            return task
        except todotask.DoesNotExist:
            return Response(status=HTTP_400_BAD_REQUEST)
    if request.method=='GET':
        task=get_pk(pk)
        serializer_obj=taskserializer(task)
        return Response(serializer_obj.data,status=HTTP_200_OK)
    if request.method=='DELETE':
        task=get_pk(pk)
        task.delete()
        return Response(status=HTTP_200_OK)
    if request.method=="PUT":
        task=get_pk(pk)
        taskobj=taskserializer(task,data=request.data)
        if taskobj.is_valid():
            taskobj.save()
            return Response(status=HTTP_200_OK)
        else:
            return Response(status=HTTP_400_BAD_REQUEST)            


