from django.urls import path
from .views import ItemList, HelloWorldView, LombardModelAPIView

urlpatterns = [
    path('api/items/', ItemList.as_view(), name='item-list'),
    path('api/hello/', HelloWorldView.as_view(), name='hello-world'),
    path('api/lombard/', LombardModelAPIView.as_view(), name='lombard'),
]