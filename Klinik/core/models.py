from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify

# Create your models here.

class Contactinfo(models.Model):
    address = models.CharField(max_length=255, blank=True, null=True)
    time = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=16, blank=True, null=True)
    email = models.EmailField(max_length=255, blank=True, null=True)
    facebook_link = models.CharField(max_length=100, blank=True, null=True)
    twitter_link = models.CharField(max_length=100, blank=True, null=True)
    linkedin_link = models.CharField(max_length=100, blank=True, null=True)
    instagram_link = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Contact Info'

    def __str__(self):
        return self.email
    

class Slider(models.Model):
    image = models.ImageField(upload_to='banner/')
    title = models.CharField(max_length=255, blank=True, null=True)
    
    class Meta:
        verbose_name_plural = 'Slider'

    def __str__(self):
        return self.title
    


class Banner(models.Model):
    banner_title = models.CharField(max_length=255, blank=True, null=True)
    doctor = models.IntegerField(blank=True, null=True)
    stuff = models.IntegerField(blank=True, null=True)
    patient = models.IntegerField(blank=True, null=True)
    created = models.DateField(auto_now_add=True)
    slider = models.ManyToManyField(Slider)

    class Meta:
        verbose_name_plural = 'Banners'
        ordering = ('-created',)

    def __str__(self):
        return self.banner_title

class Keypoints(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Key Points'

    def __str__(self):
        return self.title

class About(models.Model):
    main_image = models.ImageField(upload_to='about/', blank=True, null=True)
    image = models.ImageField(upload_to='about/', blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField()
    points = models.ManyToManyField(Keypoints)

    class Meta:
        verbose_name_plural = 'About'

    def __str__(self):
        return self.title


class Service(models.Model):
    icon = models.ImageField(upload_to='service/', blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
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


class Doctor(models.Model):
    image = models.ImageField(upload_to='doctors/', blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    dept = models.CharField(max_length=255, blank=True, null=True)
    facebook_link = models.CharField(max_length=100, blank=True, null=True)
    twitter_link = models.CharField(max_length=100, blank=True, null=True)
    linkedin_link = models.CharField(max_length=100, blank=True, null=True)
    instagram_link = models.CharField(max_length=100, blank=True, null=True)
    slug = models.SlugField(null=False, allow_unicode=True, db_index=True, blank=True, unique=True)
    created = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Doctors'
        ordering = ('-created',)
    
    def save(self, *args, **kwargs):
        # Use a custom slugify function if desired
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('core:doctors', args=[self.slug])


class Appointment(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(max_length=255, blank=True, null=True)
    mobile = models.EmailField(max_length=255, blank=True, null=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    problem = models.TextField()

    class Meta:
        verbose_name_plural = 'Appointment'

    def __str__(self):
        return self.email


class Testimonial(models.Model):
    image = models.ImageField(upload_to='testimonial/', blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    profession = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    slug = models.SlugField(null=False, allow_unicode=True, db_index=True, blank=True, unique=True)
    created = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Testimonial'
        ordering = ('-created',)
        
    def save(self, *args, **kwargs):
        # Use a custom slugify function if desired
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('core:testimonial', args=[self.slug])


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
        return reverse('core:contact', args=[self.slug])


class Newslatter(models.Model):
    email = models.EmailField(max_length=255, blank=True, null=True)
    created = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Newslatter'
        ordering = ('-created',)

    def __str__(self):
        return self.email
