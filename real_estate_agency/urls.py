from django.urls import path, re_path
from django.contrib import admin

from property import views

urlpatterns = [
    path('', views.show_flats, name='home'),
    path('search/', views.show_flats, name='search'),
    path('admin/', admin.site.urls),
]
