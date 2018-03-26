from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('restaurant/', views.restaurant_archive),
    path('restaurant/<int:restId>/', views.restaurant),
    path('restaurant/<slug:slug>/', views.menu),
]
