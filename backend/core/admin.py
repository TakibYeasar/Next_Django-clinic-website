from django.contrib import admin

from .models import (
    Banner,
    Hero,
    About,
    Service,
    Whychoose,
    Doctor,
    Contactinfo,
    Appointment,
    Testimonial,
    Contact,
)

admin.site.register([
    Banner,
    Hero,
    About,
    Service,
    Whychoose,
    Doctor,
    Contactinfo,
    Appointment,
    Testimonial,
    Contact,
])