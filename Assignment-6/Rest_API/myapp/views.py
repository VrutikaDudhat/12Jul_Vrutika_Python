from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Book
from .serailizers import *
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['POST'])
def insertdata(request):
    if request.method=="POST":
        serial=BookSerailizer(data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(data=serial.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])     
def getall(request):
    alldata=Book.objects.all()
    serial=BookSerailizer(alldata,many=True)
    return Response(data=serial.data)

@api_view(['GET'])
def getid(request,id):
    try:
        stid=Book.objects.get(id=id)
    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serial=BookSerailizer(stid)
    return Response(data=serial.data)

@api_view(["POST"])
def savedata(request):
    if request.method=='POST':
        serial=BookSerailizer(data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE','GET'])
def deleteid(request,id):
    try:
        id=Book.objects.get(id=id)
    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method=='GET':
        serial=BookSerailizer(id)
        return Response(data=serial.data)
    
    if request.method=='DELETE':
        Book.delete(id)
        return Response(status=status.HTTP_202_ACCEPTED)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['PUT','GET'])
def updatedata(request,id):
      try:
        stid=Book.objects.get(id=id)
      except Book.DoesNotExist:
          return Response(status=status.HTTP_400_BAD_REQUEST)
      
      if request.method=="GET":
          serial=BookSerailizer(stid)
          return Response(data=serial.data)
      
      if request.method=="PUT":
          serial=BookSerailizer(data=request.data,instance=stid)
          if serial.is_valid():
              serial.save()
              return Response(status=status.HTTP_202_ACCEPTED)
          else:
            return Response(status=status.HTTP_400_BAD_REQUEST)