from django.urls import path
from linker import views



urlpatterns = [
    path('', views.form_view, name= 'form_view'),
    path('<str:pk>/', views.go, name = 'go')
]
