from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.views import APIView

from .models import Item, LombardModel
from .serializers import ItemSerializer, HelloWorldSerializer, LombardModelSerializer


class ItemList(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class HelloWorldView(APIView):
    def get(self, request):
        data = {'message': 'HELLO OAOAOAO'}
        serializer = HelloWorldSerializer(data)
        return render(request, 'hello_world.html', {'message': serializer.data['message']})


@api_view(['GET'])
def export_data(request):
    data = LombardModel.objects.all()
    serializer = LombardModelSerializer(data, many=True)
    json_data = serializer.data

    # Save json_data to a file
    # Add logic to save the data to a file on your PC

    return JsonResponse({'success': True})
