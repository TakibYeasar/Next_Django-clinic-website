from django.urls import path
from .views import *

urlpatterns = [
    path('contactinfo/', ContactinfoView.as_view(), name='contactinfo-list'),
    path('banner/', BannerView.as_view(), name='banner-list'),
    path('about/', AboutView.as_view(), name='about-list'),
    path('service/', ServiceView.as_view(), name='service-list'),
    path('whychoose/', WhychooseView.as_view(), name='whychoose-list'),
    path('doctor/', DoctorView.as_view(), name='doctor-list'),
    path('testimonial/', TestimonialView.as_view(), name='testimonial-list'),
    path('contact/', ContactView.as_view(), name='contact-create'),
]
