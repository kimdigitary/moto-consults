from rest_framework.decorators import api_view, parser_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from .models import Customer, CompanySettings, Job, JobPosition, CompanySettings, EmployerCompany, RecruitmentProcess, RegistrationFees, ConsultationFees, FeesPayment
from .serializers import UserSerializer, create_standard_response, CompanySettingsSerializer, CustomerSerializer,JobPositionSerializer, JobSerializer, EmployerCompanySerializer, RecruitmentProcessSerializer, ConnectionFeesSerializer, FeesPaymentSerializer, RegistrationFeesSerializer, ConsultationFeesSerializer
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q




# DEALING WITH REGISTRATION FEES
# @api_view(['POST'])
# def add_registration_fee(request):
#     if request.method == 'POST':
#         serializer = RegistrationFeesSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return create_standard_response(status=status.HTTP_201_CREATED, message="Registration fee created successfully", data=serializer.data)
#         return create_standard_response(status=status.HTTP_400_BAD_REQUEST, message="Failed to create registration fee", data=serializer.errors)


# @api_view(['POST'])
# def add_registration_fee(request):
#     serializer = RegistrationFeesSerializer(data=request.data)
#     if serializer.is_valid():
#         # Attempt to update or create the RegistrationFees instance
#         registration_fee, created = RegistrationFees.objects.update_or_create(
#             customer=serializer.validated_data['customer'],
#             defaults={
#                 'fees_name': serializer.validated_data['fees_name'],
#                 'fees_amount': serializer.validated_data['fees_amount'],
#             }
#         )
#         if created:
#             return create_standard_response(status=status.HTTP_201_CREATED, message="Registration fee created successfully", data=serializer.data)
#         else:
#             return create_standard_response(status=status.HTTP_200_OK, message="Registration fee updated successfully", data=serializer.data)
#     return create_standard_response(status=status.HTTP_400_BAD_REQUEST, message="Failed to create registration fee", data=serializer.errors)


@api_view(['POST'])
def add_registration_fee(request):
    user = request.user 
    
    # Checking if a RegistrationFees instance already exists for this user
    existing_fee = RegistrationFees.objects.filter(user=user).first()
    
    if existing_fee:
        # Updating the existing RegistrationFees instance
        serializer = RegistrationFeesSerializer(existing_fee, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return create_standard_response(status=status.HTTP_200_OK, message="Registration fee updated successfully", data=serializer.data)
    else:
        # Creating a new RegistrationFees instance
        serializer = RegistrationFeesSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=user)
            return create_standard_response(status=status.HTTP_201_CREATED, message="Registration fee created successfully", data=serializer.data)
    
    return create_standard_response(status=status.HTTP_400_BAD_REQUEST, message="Failed to create/update registration fee", data=serializer.errors)
   