from django.contrib import admin
from django.urls import path, include
from django.views.generic import detail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/', include('base.urls', namespace='base')),

]
