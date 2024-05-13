from django.urls import path
from . import views

app_name = 'base'

urlpatterns = [
    path('', views.note_list, name='note_list'),
    path('<int:pk>/', views.note_detail, name='note_detail'),
]
