from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import send_mail

# Create your views here.

class ContactinfoView(APIView):
    def get(self, request):
        try:
            info_obj = Contactinfo.objects.all()
            info_serializer = ContactinfoSerializer(
                info_obj, many=True, context={'request': request}).data
            return Response(info_serializer, status=status.HTTP_201_CREATED)
        except ObjectDoesNotExist:
            return Response({'error': 'No contact info found'}, status=status.HTTP_404_NOT_FOUND)


class BannerView(APIView):
    def get(self, request):
        try:
            banner_obj = Banner.objects.all()
            banner_serializer = BannerSerializer(
                banner_obj, many=True, context={'request': request}).data
            data = []
            for items in banner_serializer:
                item_obj = Slider.objects.all()
                items['slider'] = SliderSerializer(
                    item_obj, context={'request': request}, many=True).data
                data.append(items)
            return Response(data, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return Response({'error': 'No banner found'}, status=status.HTTP_404_NOT_FOUND)


class AboutView(APIView):
    def get(self, request):
        try:
            about_obj = About.objects.all()
            about_serializer = AboutSerializer(
                about_obj, many=True, context={'request': request}).data
            data = []
            for items in about_serializer:
                item_obj = Keypoints.objects.all()
                items['points'] = KeypointsSerializer(
                    item_obj, context={'request': request}, many=True).data
                data.append(items)
            return Response(data, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return Response({'error': 'No about found'}, status=status.HTTP_404_NOT_FOUND)


class ServiceView(APIView):
    def get(self, request):
        try:
            service_obj = Service.objects.all()
            service_serializer = ServiceSerializer(
                service_obj, many=True, context={'request': request}).data
            return Response(service_serializer, status=status.HTTP_201_CREATED)
        except ObjectDoesNotExist:
            return Response({'error': 'No service found'}, status=status.HTTP_404_NOT_FOUND)


class WhychooseView(APIView):
    def get(self, request):
        try:
            whychoose_obj = Whychoose.objects.all()
            whychoose_serializer = WhychooseSerializer(
                whychoose_obj, many=True, context={'request': request}).data
            return Response(whychoose_serializer, status=status.HTTP_201_CREATED)
        except ObjectDoesNotExist:
            return Response({'error': 'No whychoose found'}, status=status.HTTP_404_NOT_FOUND)


class DoctorView(APIView):
    def get(self, request):
        try:
            doctor_obj = Doctor.objects.all()
            doctor_serializer = DoctorSerializer(
                doctor_obj, many=True, context={'request': request}).data
            return Response(doctor_serializer, status=status.HTTP_201_CREATED)
        except ObjectDoesNotExist:
            return Response({'error': 'No doctor found'}, status=status.HTTP_404_NOT_FOUND)


class TestimonialView(APIView):
    def get(self, request):
        try:
            test_obj = Testimonial.objects.all()
            test_serializer = TestimonialSerializer(
                test_obj, many=True, context={'request': request}).data
            return Response(test_serializer, status=status.HTTP_201_CREATED)
        except ObjectDoesNotExist:
            return Response({'error': 'No test found'}, status=status.HTTP_404_NOT_FOUND)


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
