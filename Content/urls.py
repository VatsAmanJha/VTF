from django.urls import path,include
from .views import journal_detail
urlpatterns = [
    path('journal/<int:journal_id>/', journal_detail, name='journal_detail'),
]
