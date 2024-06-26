from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.Home,name="home"),
    path('getStarted/',views.GetStarted,name='get-started'),
    path('about/',views.About,name='about'),
    path('contact/',views.Contact,name='contact'),
    path('pricing/',views.Pricing,name='pricing'),
    path('trainers/',views.Trainers,name='trainers'),
    path('events/',views.Events,name='events'),
    path('counts/',views.Counts,name='counts'),


]