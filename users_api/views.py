from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token

from .models import User
from .serializers import UserSerializer, ItemSerializer

from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your views here.
@receiver(post_save, sender=User)
def generate_token(sender, instance = None, created = False, **kwargs):
    if created:
        Token.objects.create(user=instance)



@api_view(["GET","POST"])
def user_list(request):
    if request.method == "GET":
        users = UserSerializer(instance=User.objects.all(), many=True)
        return Response(data=users.data, status=status.HTTP_200_OK)
    else:
        # allow front-end to pass some fields and some fields remain empty
        user = UserSerializer(data=request.data, partial=True)
        # verify data
        if user.is_valid():
            user.save()
            return Response(data=user.data, status=status.HTTP_200_OK)
        else:
            return Response(user.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET","PUT","DELETE","PATCH"])
def user_detail(request, pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(data = {"msg": "User does not found"}, status = status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        user = UserSerializer(instance=user)

        return Response(data=user.data, status=status.HTTP_200_OK)

    elif request.method == "PUT":
        user = UserSerializer(instance=user, data=request.data)
        if user.is_valid():
            user.save()
            return Response(data=user.data, status=status.HTTP_200_OK)
        return Response(user.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == "PATCH":
        user = UserSerializer(instance=user, data=request.data, partial=True)
        if user.is_valid():
            user.save()
            return Response(data=user.data, status=status.HTTP_200_OK)
        return Response(user.errors, status=status.HTTP_400_BAD_REQUEST)




