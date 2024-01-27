import json

from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Item
from .serializers import ItemSerializer, HelloWorldSerializer, LombardModelSerializer
from django.shortcuts import render


class ItemList(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class HelloWorldView(APIView):
    def get(self, request):
        data = {'message': 'HELLO WORLD'}
        serializer = HelloWorldSerializer(data)
        return render(request, 'hello_world.html', {'message': serializer.data['message']})


class LombardModelAPIView(APIView):
    def get(self, request):
        try:
            with open('/Users/tisenres/PycharmProjects/uzInfoScanBack/uzInfoScanBack/uzInfoScanBackApp/datasets/lombard.json', 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            return Response({"error": "File not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = LombardModelSerializer(data=data, many=True)

        if serializer.is_valid():
            lombard_data = serializer.data
            return render(request, '/Users/tisenres/PycharmProjects/uzInfoScanBack/uzInfoScanBack/uzInfoScanBackApp/templates/lombard.html', {'lombard_data': lombard_data})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def post(self, requests):
        with open('/Users/tisenres/PycharmProjects/uzInfoScanBack/uzInfoScanBack/uzInfoScanBackApp/datasets/lombard.json','r') as file:
            data = json.load(file)

        serializer = LombardModelSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
