from django.urls import path
from . import views

app_name = 'product'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('add', views.add_products, name='add_products'),
    path('<str:slug>/edit', views.edit_product, name='edit_product'),
    path('<str:slug>', views.product_details, name='product_details'),
    path('<str:slug>/like_dislike', views.like_dislike, name='like_dislike'),
]
