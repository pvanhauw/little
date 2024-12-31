from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('api/menu-items/', views.MenuItemsView.as_view(), name='menu-items'),
    path('api/menu-items/<int:pk>', views.SingleMenuItemView.as_view()),
    path('api/bookings/', views.BookingView.as_view(), name='bookings'),
    path('api/bookings/<int:pk>', views.SingleBookingView.as_view(), name='single-booking'),
    path('api-token-auth/', obtain_auth_token),
    path('', views.index, name='index'),
]
