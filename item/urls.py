from django.urls import path

from item import views

app_name = 'item'

urlpatterns = [
    path('<int:pk>', views.detail, name='detail'),
    path('new/', views.new, name='new'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/edit/', views.edit, name='edit'),
    path('items/', views.items, name='items'),

]