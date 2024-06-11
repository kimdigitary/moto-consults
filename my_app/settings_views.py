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


@api_view(['POST', 'PUT'])
@parser_classes([MultiPartParser, FormParser])
def company_settings_view(request):
    if request.method == 'POST':
        serializer = CompanySettingsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return create_standard_response(status=status.HTTP_201_CREATED, message="Company settings created successfully", data=serializer.data)
        return create_standard_response(status=status.HTTP_400_BAD_REQUEST, message="Invalid data", data=serializer.errors)

    elif request.method == 'PUT':
        try:
            company_setting = CompanySettings.objects.get(pk=request.data['id'])
        except CompanySettings.DoesNotExist:
            return create_standard_response(status=status.HTTP_404_NOT_FOUND, message="Company settings not found")

        serializer = CompanySettingsSerializer(company_setting, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return create_standard_response(status=status.HTTP_200_OK, message="Company settings updated successfully", data=serializer.data)
        return create_standard_response(status=status.HTTP_400_BAD_REQUEST, message="Invalid data", data=serializer.errors)




# DEALING WITH SETTINGS 
@api_view(['POST'])
def add_settings(request):
    if request.method == 'POST':
        serializer = CompanySettingsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return create_standard_response(status=status.HTTP_201_CREATED, message="Settings created successfully", data=serializer.data)
        return create_standard_response(status=status.HTTP_400_BAD_REQUEST, message="Failed to create settings", data=serializer.errors)


@api_view(['GET', 'PUT'])
def edit_settings(request, pk):
    try:
        setting = CompanySettings.objects.get(pk=pk)
    except CompanySettings.DoesNotExist:
        return create_standard_response(status=status.HTTP_404_NOT_FOUND, message="settings not found")

    if request.method == 'GET':
        serializer = CompanySettingsSerializer(setting)
        return create_standard_response(status=status.HTTP_200_OK, message="Settings retrieved successfully", data=serializer.data)

    elif request.method == 'PUT':
        serializer = CompanySettingsSerializer(setting, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return create_standard_response(status=status.HTTP_200_OK, message="Job position updated successfully", data=serializer.data)
        return create_standard_response(status=status.HTTP_400_BAD_REQUEST, message="Failed to update job position details", data=serializer.errors)


@api_view(['GET'])
def get_jobposition(request, pk):
    try:
        jobposition = JobPosition.objects.get(pk=pk)
    except JobPosition.DoesNotExist:
        return create_standard_response(status=status.HTTP_404_NOT_FOUND, message="Job position not found")

    if request.method == 'GET':
        serializer = JobPositionSerializer(jobposition)
        return create_standard_response(status=status.HTTP_200_OK, message="Job position details retrieved successfully", data=serializer.data)

