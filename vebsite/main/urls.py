from django.urls import path
from .import views

urlpatterns = [
    path ('',views.index ),
    path ('about', views.about),
    path ('home/', views.home),
    path ('new-page', views.new),
]
