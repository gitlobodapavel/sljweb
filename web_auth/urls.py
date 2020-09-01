from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.registration, name='registration_view'),
    path('login/', views.login, name='login_view'),
    path('logout/', views.logout, name='logout_view'),
    path('activate/<slug:uidb64>/<slug:token>/', views.activate, name='activate'),
    path('confirm/', views.confirm, name='confirm_info_view'),
]