from django.shortcuts import render
from django.http import JsonResponse
from .serializers import userSerializer
from .models import user
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User, auth
from django.contrib import messages
from rest_framework import status


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

    # if request.method == 'POST':
    #     email = request.data.get('email')
    #     # password = request.data.get('password')
    #     try:
    #         us = user.objects.get(email=email)
    #         if us.email == None:
    #             newUser = user(data=request.data)
    #             newUser.save()
    #             return Response(status=status.HTTP_200_OK)
    #         else:
    #             return Response(status=status.HTTP_400_BAD_REQUEST)
    #     except user.DoesNotExist:
    #         serializer = userSerializer(data=request.data)
    #         if serializer.is_valid():
    #             serializer.save()
    #         return Response(status=status.HTTP_404_NOT_FOUND)
    #     except Exception as e:
    #         print("Other err", e)
    #         return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
def listUsers(request):
    print(request)
    if request.method == 'POST':
        email = request.data.get('email')
        password = request.data.get('password')
        try:
            us = user.objects.get(email=email)
            if us.email == email and us.password == password:
                return Response(status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        except user.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            print("Other err", e)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@ api_view(['POST'])
def updateUser(request, pk):
    one_user = user.objects.get(id=pk)
    serializer = userSerializer(instance=one_user, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@ api_view(['DELETE'])
def deleteuser(request, pk):
    one_user = user.objects.get(id=pk)
    one_user.delete()

    return Response('user has been succsesfully deleted !!')


# def user_exist(username):
