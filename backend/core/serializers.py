from rest_framework import serializers
from .models import *

class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = "__all__"

    def imageurl(self, obj):
        request = self.obj.get('request')
        return request.url("image")


class HeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hero
        fields = "__all__"



class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = "__all__"

    def imageurl(self, obj):
        request = self.obj.get('request')
        return request.url("image")



class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = "__all__"

    def imageurl(self, obj):
        request = self.obj.get('request')
        return request.url("image")



class WhychooseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Whychoose
        fields = "__all__"

    def imageurl(self, obj):
        request = self.obj.get('request')
        return request.url("image")



class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = "__all__"

    def imageurl(self, obj):
        request = self.obj.get('request')
        return request.url("image")



class ContactinfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contactinfo
        fields = "__all__"


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = "__all__"



class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = "__all__"

    def imageurl(self, obj):
        request = self.obj.get('request')
        return request.url("image")




class ContactSerialier(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'




