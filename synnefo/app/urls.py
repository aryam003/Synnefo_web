from django.urls import path
from . import views


urlpatterns = [
    path('',views.home),  
    path('contact',views.contact),
    path('courses',views.courses),
    path('placement',views.placement),
    path('about',views.about),
]