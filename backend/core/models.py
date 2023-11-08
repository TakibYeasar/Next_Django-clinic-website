from django.db import models
from authapi.models import CustomUser
from django.shortcuts import reverse

# Create your models here.

class Banner(models.Model):
    image = models.ImageField(upload_to='banner/')
    title = models.CharField(max_length=255, blank=True, null=True)
    slug = models.SlugField(blank=True, null=True)
    created = models.DateField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'Banners'
        ordering = ('-created',)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("core:banner", kwargs={
            'slug': self.slug
        })

class Hero(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    doctor = models.CharField(max_length=255, blank=True, null=True)
    stuff = models.CharField(max_length=255, blank=True, null=True)
    patient = models.CharField(max_length=255, blank=True, null=True)
    banner = models.ManyToManyField(Banner, blank=True, null=True)
    
    class Meta:
        verbose_name_plural = 'Hero'

    def __str__(self):
        return self.title


class About(models.Model):
    main_image = models.ImageField(upload_to='about/', blank=True, null=True)
    image = models.ImageField(upload_to='about/', blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField()
    
    class Meta:
        verbose_name_plural = 'About'

    def __str__(self):
        return self.title


class Service(models.Model):
    icon = models.ImageField(upload_to='service/', blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    slug = models.SlugField(blank=True, null=True)
    created = models.DateField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'Service'
        ordering = ('-created',)

    def __str__(self):
        return self.title


class Whychoose(models.Model):
    image = models.ImageField(upload_to='whychoose/', blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    
    class Meta:
        verbose_name_plural = 'Why Choose'

    def __str__(self):
        return self.image



class Doctor(models.Model):
    image = models.ImageField(upload_to='doctors/', blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    dept = models.CharField(max_length=255, blank=True, null=True)
    slug = models.SlugField(blank=True, null=True)
    created = models.DateField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'Doctors'
        ordering = ('-created',)

    def __str__(self):
        return self.image
    
    def get_absolute_url(self):
        return reverse("core:doctors", kwargs={
            'slug': self.slug
        })


class Contactinfo(models.Model):
    description = models.TextField(blank=True, null=True)
    phone = models.CharField(max_length=16, blank=True, null=True)
    email = models.EmailField(max_length=255, blank=True, null=True)
    
    class Meta:
        verbose_name_plural = 'Contact Info'

    def __str__(self):
        return self.email



class Appointment(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(max_length=255, blank=True, null=True)
    phone = models.EmailField(max_length=255, blank=True, null=True)
    date = models.DateField()
    time = models.DateTimeField()
    
    class Meta:
        verbose_name_plural = 'Appointment'

    def __str__(self):
        return self.email



class Testimonial(models.Model):
    image = models.ImageField(upload_to='testimonial/', blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    profession = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    slug = models.SlugField(blank=True, null=True)
    created = models.DateField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'Testimonial'
        ordering = ('-created',)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("core:testimonial", kwargs={
            'slug': self.slug
        })




class Contact(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(max_length=50, blank=True, null=True)
    subject = models.CharField(max_length=100, blank=True, null=True)
    message = models.TextField(blank=True)
    
    class Meta:
        verbose_name_plural = 'Contact'
    
    def __str__(self):
        return self.email
    
    def get_absolute_url(self):
        return reverse("core:contact", kwargs={
            'slug': self.slug
        })




