from django.urls import path
from . import views

app_name = 'hello'

urlpatterns = [
    path('', views.index, name='index'), 
    path('edit/<int:book_id>/', views.edit, name='edit'),
    path('delete/<int:book_id>/', views.delete, name='delete'),
    path('insert/', views.insert, name='insert'),
    path('update/<int:book_id>/', views.update, name='update'),
]