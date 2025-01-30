from django.urls import path
from . import views


app_name = 'categories'

urlpatterns = [
    path('categories/', views.category_list, name='category_list'),
    path('detail/<int:year>/<int:month>/<int:day>/<slug:slug>/', views.category_detail, name='detail'),
    path('categories/create/', views.category_create, name='category_create'),
    path('categories/<int:pk>/update/', views.category_update, name='update'),
    path('categories/<int:pk>/delete/', views.category_delete, name='delete'),
]