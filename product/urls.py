from django.urls import path

from . import views

urlpatterns = [
    path('<int:pk>/',views.product_detail_view,name='products-list'),
    path('<int:pk>/update',views.product_update_view,name='products-edit'),
    path('<int:pk>/destroy',views.product_destroy_view),
    path('',views.product_list_create_view,name='products-detail'),
    path('create/',views.product_list_create_view),
]