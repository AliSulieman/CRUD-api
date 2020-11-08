from django.shortcuts import render
from django.http import JsonResponse
from .serializers import userSerializer
from .models import user
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'create': '/user/create'
    }
    return Response(api_urls)


@api_view(['POST'])
def adduser(request):
    serializer = userSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['GET'])
def listUsers(request):
    users = user.objects.all()
    serializer = userSerializer(users, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def updateUser(request, pk):
    one_user = user.objects.get(id=pk)
    serializer = userSerializer(instance=one_user, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def deleteuser(request, pk):
    one_user = user.objects.get(id=pk)
    one_user.delete()

    return Response('user has been succsesfully deleted !!')


# def user_exist(username):
