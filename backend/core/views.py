from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import send_mail

# Create your views here.


class BannerView(APIView):
    def get(self, request):
        banner_obj = Banner.objects.all()
        banner_serializers = BannerSerializer(banner_obj, many=True, context={'request':request}).data
        return Response(banner_serializers)


class HeroView(APIView):
    def get(self, request):
        hero_obj = Hero.objects.all()
        hero_serializers = HeroSerializer(hero_obj, many=True, context={'request':request}).data
        return Response(hero_serializers)



class AboutView(APIView):
    def get(self, request):
        about_obj = About.objects.all()
        about_serializers = AboutSerializer(about_obj, many=True, context={'request':request}).data
        return Response(about_serializers)



class ServiceView(APIView):
    def get(self, request):
        service_obj = Service.objects.all()
        service_serializers = ServiceSerializer(service_obj, many=True, context={'request':request}).data
        return Response(service_serializers)



class WhychooseView(APIView):
    def get(self, request):
        whychoose_obj = Whychoose.objects.all()
        whychoose_serializers = WhychooseSerializer(whychoose_obj, many=True, context={'request':request}).data
        return Response(whychoose_serializers)


class DoctorView(APIView):
    def get(self, request):
        doctor_obj = Doctor.objects.all()
        doctor_serializers = DoctorSerializer(doctor_obj, many=True, context={'request':request}).data
        return Response(doctor_serializers)



class ContactinfoView(APIView):
    def get(self, request):
        info_obj = Contactinfo.objects.all()
        info_serializers = ContactinfoSerializer(info_obj, many=True, context={'request':request}).data
        return Response(info_serializers)



class TestimonialView(APIView):
    def get(self, request):
        test_obj = Testimonial.objects.all()
        test_serializers = TestimonialSerializer(test_obj, many=True, context={'request':request}).data
        return Response(test_serializers)





class ContactView(APIView):
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [TokenAuthentication, ]

    def post(self, request, format=None):
        data = self.request.data
        response = 'You will be contacted shortly.'

        try:
            send_mail(data['subject'],
                      'Name: ' + data['name'] + '\nEmail: ' + data['email'] +
                      '\n\nMessage:\n' + data['message'] + '\n\n' + response,
                      '19bcp101.nepal@gmail.com',
                      [data['email'], 'nothing3669@gmail.com'],
                      fail_silently=False)

            contact = Contact(name=data['name'],
                              email=data['email'],
                              subject=data['subject'],
                              message=data['message'])
            contact.save()

            return Response({'success': 'Message sent successfully'})

        except:
            return Response({'error': 'Message failed to send'})