from django import views
from django.urls import path
from .views import *

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('todo/<int:pk>/', TodoDetail.as_view(), name='todo'),
    path('update/<int:pk>/', TodoUpdate.as_view(), name='update'),
    path('delete/<int:pk>/', TodoDelete.as_view(), name='delete'),
    path('create/', TodoCreate.as_view(), name='create'),
]