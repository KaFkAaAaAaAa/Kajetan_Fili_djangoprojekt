from django.urls import path
from . import views

app_name = 'base'

urlpatterns = [
    path('', views.notes_list, name='notes_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:note>/', views.note_detail, name='note_detail'),
]
