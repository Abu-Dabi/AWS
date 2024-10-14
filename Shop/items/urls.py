from django.urls import path
from .views import *

urlpatterns = [
    path('', category_list),
    path('contacts/', contacts),
    path('category/detail/<int:id>', item_list),
    path('item/detail/<int:id>', item_detail),
    path('register/', site_register),
    path('login/', site_login),
    path('logout/', site_logout)
]
