from django.urls import path
from .views import *

urlpatterns = [
    path('', BaseView.as_view(), name='index'),
    path('categories/<str:slug>', CategoryView.as_view(), name='category')
]