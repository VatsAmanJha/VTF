from django.urls import path,include
from Main import views

urlpatterns = [
    path('',views.index,name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('journal/', views.journal, name='journal'),
]
