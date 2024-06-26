from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', views.Welcome,name="welcome"),
    path('account/', views.Account,name="account"),
    path('otp_verification/',views.otp_verification,name="otp_verification"),
    path('more-details/<int:user_id>/', views.MoreDetails, name="more_details"),
    path('logout/',views.Logout,name='logout'),

]