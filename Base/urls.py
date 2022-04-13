from .views import index, detail

from django.urls import path

urlpatterns = [
    path('', index, name='index'),
    path('<str:id>/', detail, name='detail')
]