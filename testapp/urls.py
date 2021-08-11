from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('update/<int:pk>', views.Update,name='Update'),
    path('create/', views.Create,name='Create'),
    path('delete/<int:pk>', views.Delete,name='Delete'),
]
