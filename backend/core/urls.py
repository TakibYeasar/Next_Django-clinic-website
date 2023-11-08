from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('banners/', BannerView.as_view()),
    path('hero/', HeroView.as_view()),
    path('about/', AboutView.as_view()),
    path('service/', ServiceView.as_view()),
    path('whychoose/', WhychooseView.as_view()),
    path('doctor/', DoctorView.as_view()),
    path('contactinfo/', ContactinfoView.as_view()),
    path('testimonial/', TestimonialView.as_view()),
    path('contact/', ContactView.as_view()),
]
