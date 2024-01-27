import json

from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Item
from .serializers import ItemSerializer, HelloWorldSerializer, LombardModelSerializer


class ItemList(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class HelloWorldView(APIView):
    def get(self, request):
        data = {'message': 'HELLO OAOAOAO'}
        serializer = HelloWorldSerializer(data)
        return render(request, 'hello_world.html', {'message': serializer.data['message']})


class LombardModelAPIView(APIView):
    def post(self):
        # Read the JSON file
        with open('datasets/lombard.json', 'r') as file:
            data = json.load(file)

        # Deserialize JSON data using the serializer
        serializer = LombardModelSerializer(data=data)
        if serializer.is_valid():
            # Save the deserialized data to the database
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)