from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),

    path('restaurants/', views.restaurant_list, name='restaurant_list'),
    path('restaurants/<int:restaurant_id>/',
         views.restaurant_detail, name='restaurant_detail'),

    path('restaurants/<int:restaurant_id>/create_reservation/',
         views.create_reservation, name='create_reservation'),

    path('reservation_success/', views.reservation_success,
         name='reservation_success'),

    path('restaurants/<int:restaurant_id>/leave_review/',
         views.leave_review, name='leave_review'),

    path('reservations/', views.my_reservations, name='reservations'),

    path('register/', views.user_registration, name='user_registration'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('register_restaurant/', views.restaurant_registration,
         name='restaurant_registration'),

    # Profile
    path('profile/', views.user_profile, name='user_profile'),

    # Search Url
    path('search/', views.search_view, name='search'),
]
