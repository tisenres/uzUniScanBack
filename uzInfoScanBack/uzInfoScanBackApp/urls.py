from django.urls import path
from .views import ItemList, HelloWorldView, export_data

urlpatterns = [
    path('api/items/', ItemList.as_view(), name='item-list'),
    path('api/hello/', HelloWorldView.as_view(), name='hello-world'),
    path('export_data/', export_data, name='export_data'),
]