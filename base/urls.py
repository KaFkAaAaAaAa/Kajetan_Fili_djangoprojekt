from base import views
from django.urls import path

app_name = 'base'

urlpatterns = [
    path('', views.note_list, name='note_list'),
    path('<int:pk>/', views.note_detail, name='note_detail'),
    path('create_temp/', views.create_note, name='create_temp')
]
