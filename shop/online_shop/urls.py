from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('register/', views.register_view, name = 'register'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),
    path('profile/', views.profile_view, name='profile'),
    path('service/', views.service_list_view, name='service_list'),
    path('service/<int:id>/', views.service_detail_view, name='service_detail'),
    path('search_result/', views.search_result_view, name='search_result'),
    

    
]