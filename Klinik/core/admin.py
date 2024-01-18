from django.contrib import admin

from .models import (
    Contactinfo,
    Slider,
    Banner,
    Keypoints,
    About,
    Service,
    Whychoose,
    Doctor,
    Appointment,
    Testimonial,
    Contact,
    Newslatter,
)

admin.site.register([
    Contactinfo,
    Slider,
    Banner,
    Keypoints,
    About,
    Service,
    Whychoose,
    Doctor,
    Appointment,
    Testimonial,
    Contact,
    Newslatter,
])
