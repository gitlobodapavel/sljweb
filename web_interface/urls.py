from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.profile, name='profile_view'),
    path('newpet/', views.newpet, name='pet_reg_view'),
    path('pet/<int:pk>', views.pet_profile, name='pet_profile_view'),
    path('delete_pet/<int:pk>', views.delete_pet_profile, name='remove_pet_profile_view'),
    path('edit_pet/<int:pk>', views.edit_pet_profile, name='edit_pet_profile_view'),
    path('edit_profile/<int:pk>', views.edit_user_profile, name='edit_user_profile_view'),
    path('newproduct', views.newpoduct, name='create_product_view'),
    path('edit_product/<int:pk>', views.edit_product, name='edit_product_view'),
    path('delete_product/<int:pk>', views.delete_product, name='delete_product_view'),
    path('product/<int:pk>', views.view_product, name='product_view'),
]