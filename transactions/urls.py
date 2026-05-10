from django. urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('delete/<int:transaction_id>/', views.delete_transaction, name='delete_transaction'),
    path('register/', views.register, name='register'),

]