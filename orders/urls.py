from django.urls import path
from . import views


app_name = 'orders'

urlpatterns = [
    path('orders/', views.order_list, name='order_list'),
    path('orders/<int:pk>/', views.order_detail, name='detail'),
    path('orders/<int:pk>/update/', views.order_update, name='update'),
]