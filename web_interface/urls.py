from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.profile, name='profile_view'),
    path('newpet/', views.newpet, name='pet_reg_view'),
    path('pet/<int:pk>', views.pet_profile, name='pet_profile_view'),
    path('delete_pet/<int:pk>', views.delete_pet_profile, name='remove_pet_profile_view'),
    path('edit_pet/<int:pk>', views.edit_pet_profile, name='edit_pet_profile_view'),
]