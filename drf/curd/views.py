from django.shortcuts import render
from django.http import JsonResponse
from .serializers import userSerializer
from .models import user
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.


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
