from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<id>', views.detail, name='detail'),
    path('edit/<id>', views.edit, name='edit'),
]