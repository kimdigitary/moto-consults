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




# DEALING WITH EMPLOYER COMPANIES 
@api_view(['POST'])
def add_employer_company(request):
    if request.method == 'POST':
        serializer = EmployerCompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return create_standard_response(status=status.HTTP_201_CREATED, message="employer compnay created successfully", data=serializer.data)
        return create_standard_response(status=status.HTTP_400_BAD_REQUEST, message="Failed to create new employer company", data=serializer.errors)


@api_view(['GET', 'PUT'])
def edit_employer_company(request, pk):
    try:
        employer_company = EmployerCompany.objects.get(pk=pk)
    except EmployerCompany.DoesNotExist:
        return create_standard_response(status=status.HTTP_404_NOT_FOUND, message="Employer company not found")

    if request.method == 'GET':
        serializer = EmployerCompanySerializer(employer_company)
        return create_standard_response(status=status.HTTP_200_OK, message="Employer company details retrieved successfully", data=serializer.data)

    elif request.method == 'PUT':
        serializer = EmployerCompanySerializer(employer_company, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return create_standard_response(status=status.HTTP_200_OK, message="Employer company updated successfully", data=serializer.data)
        return create_standard_response(status=status.HTTP_400_BAD_REQUEST, message="Failed to update Employer company details", data=serializer.errors)


@api_view(['DELETE'])
def delete_employer_company(request, pk):
    try:
        employer_company = EmployerCompany.objects.get(pk=pk)
    except EmployerCompany.DoesNotExist:
        return create_standard_response(status=status.HTTP_404_NOT_FOUND, message="Employer company not found")

    if request.method == 'DELETE':
        employer_company.delete()
        return create_standard_response(status=status.HTTP_204_NO_CONTENT, message="Employer company deleted successfully")


@api_view(['GET'])
def get_employer_company(request, pk):
    try:
        employer_company = EmployerCompany.objects.get(pk=pk)
    except EmployerCompany.DoesNotExist:
        return create_standard_response(status=status.HTTP_404_NOT_FOUND, message="Employer company not found")

    if request.method == 'GET':
        serializer = EmployerCompanySerializer(employer_company)
        return create_standard_response(status=status.HTTP_200_OK, message="Employer company details retrieved successfully", data=serializer.data)
    

@api_view(['GET'])
def search_employer_company(request):
    query_params = request.query_params
    filters = Q()

    name = query_params.get('name')
    if name:
        filters &= Q(name__icontains=name)

    email = query_params.get('email')
    if email:
        filters &= Q(email__icontains=email)

    phone_number = query_params.get('phone_number')
    if phone_number:
        filters &= Q(phone_number__icontains=phone_number)

    address = query_params.get('address')
    if address:
        filters &= Q(address__icontains=address)

    employer_companies = EmployerCompany.objects.filter(filters)
    serializer = EmployerCompanySerializer(employer_companies, many=True)

    return create_standard_response(
        status=status.HTTP_200_OK,
        message="Employer company search results retrieved successfully",
        data=serializer.data
    )


