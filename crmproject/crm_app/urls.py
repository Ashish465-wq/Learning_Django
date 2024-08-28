from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact_list, name='contact_list'),
    path('contact/<int:pk>', views.contact_detail, name='contact_detail'),
    path('contact/new/', views.contact_create, name='contact_create'),
    path('contact/<int:pk>/activity/new', views.activity_create,
         name='activity_create')
]