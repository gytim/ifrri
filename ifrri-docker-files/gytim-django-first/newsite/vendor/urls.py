from django.urls import path
from . import views

urlpatterns = [
   path('', views.main_page, name='index'),
   path('vendor/create_base/', views.create_base, name='create_base'),
   path('vendor/', views.vendor_list, name='vendor_list'),
   path('vendor/<int:pk>', views.vendor_detail, name='vendor_detail'),
   path('vendor/new', views.vendor_new, name='vendor_new'),
   path('vendor/<pk>/remove/', views.vendor_remove, name='vendor_remove'),
]
