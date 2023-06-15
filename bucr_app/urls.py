from django.urls import path
from . import views

urlpatterns = [
     path('', views.homepage, name='homepage'),
     path('register/', views.user_registration, name='user_registration'),
     path('login/', views.user_login, name='login'),
     path('logout/', views.user_logout, name='logout'),
     

     # Reservations Url
     path('reservation_success/', views.reservation_success,
         name='reservation_success'),
     
     path('reservations/', views.my_reservations, name='reservations'),
     
     
     ############<<---RESTAURANT URLS --->>>################################
     path('register_restaurant/', views.restaurant_registration,
         name='restaurant_registration'),
     
     # Leave Review
     path('restaurants/<int:restaurant_id>/leave_review/',
         views.leave_review, name='leave_review'),
     
     # Restaurant Profile Edit
     path('restaurant/profile/edit/', views.edit_restaurant, 
          name='edit_restaurant'),
     
     # Restaurant's Profile Url
     path('restaurant/profile/', views.restaurant_profile, name='restaurant_profile'),


     # Restaurant List
     path('restaurants/', views.restaurant_list, name='restaurant_list'),
     
     # Restaurant Detail
     path('restaurants/<int:restaurant_id>/',
         views.restaurant_detail, name='restaurant_detail'),

     # Create Reservation
     path('restaurants/<int:restaurant_id>/create_reservation/',
         views.create_reservation, name='create_reservation'),




    # Profile
    path('profile/', views.user_profile, name='user_profile'),

    # Search Url
    path('search/', views.search_view, name='search'),
]
