from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('menu-items/', views.MenuItemsView.as_view(), name='menu-items'),
    path('menu-items/<int:pk>', views.SingleMenuItemView.as_view()),
    path('bookings/', views.BookingView.as_view(), name='bookings'),
    path('bookings/<int:pk>', views.SingleBookingView.as_view(), name='single-booking'),
    path('api-token-auth/', obtain_auth_token),
]
