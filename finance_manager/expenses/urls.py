from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_expense, name='add_expense'),
    path('update/<int:pk>/', views.update_expense, name='update_expense'),
    path('delete/<int:pk>/', views.delete_expense, name='delete_expense'),
    path('export/', views.export_csv, name='export_csv'),

]
