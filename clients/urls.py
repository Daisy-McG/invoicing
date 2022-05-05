from django.urls import path
from . import views

urlpatterns = [
    path('', views.ClientView.as_view(), name="clients"),
    path('create/', views.CreateClientView.as_view(), name="create_client"),
    path('edit/<slug:pk>/', views.EditClientView.as_view(), name="edit_client"),
    path('view/<slug:pk>/', views.ViewClientView.as_view(), name="view_client"),
    path('delete/<slug:pk>/', views.DeleteClientView.as_view(), name="delete_event"),
]