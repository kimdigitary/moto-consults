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



# DEALING WITH CUSTOMERS 
@api_view(['POST'])
def add_customer(request):
    if request.method == 'POST':
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return create_standard_response(status=status.HTTP_201_CREATED, message="Customer created successfully", data=serializer.data)
        return create_standard_response(status=status.HTTP_400_BAD_REQUEST, message="Failed to create customer", data=serializer.errors)


@api_view(['GET', 'PUT'])
def edit_customer(request, pk):
    try:
        customer = Customer.objects.get(pk=pk)
    except Customer.DoesNotExist:
        return create_standard_response(status=status.HTTP_404_NOT_FOUND, message="Customer not found")

    if request.method == 'GET':
        serializer = CustomerSerializer(customer)
        return create_standard_response(status=status.HTTP_200_OK, message="Customer details retrieved successfully", data=serializer.data)

    elif request.method == 'PUT':
        serializer = CustomerSerializer(customer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return create_standard_response(status=status.HTTP_200_OK, message="Customer updated successfully", data=serializer.data)
        return create_standard_response(status=status.HTTP_400_BAD_REQUEST, message="Failed to update customer", data=serializer.errors)


@api_view(['DELETE'])
def delete_customer(request, pk):
    try:
        customer = Customer.objects.get(pk=pk)
    except Customer.DoesNotExist:
        return create_standard_response(status=status.HTTP_404_NOT_FOUND, message="Customer not found")

    if request.method == 'DELETE':
        customer.delete()
        return create_standard_response(status=status.HTTP_204_NO_CONTENT, message="Customer deleted successfully")


@api_view(['GET'])
def get_customer(request, pk):
    try:
        customer = Customer.objects.get(pk=pk)
    except Customer.DoesNotExist:
        return create_standard_response(status=status.HTTP_404_NOT_FOUND, message="Customer not found")

    if request.method == 'GET':
        serializer = CustomerSerializer(customer)
        return create_standard_response(status=status.HTTP_200_OK, message="Customer details retrieved successfully", data=serializer.data)
    

@api_view(['GET'])
def search_customers(request):
    query_params = request.query_params
    filters = Q()

    firstname = query_params.get('firstname')
    if firstname:
        filters &= Q(firstname__icontains=firstname)

    othernames = query_params.get('othernames')
    if othernames:
        filters &= Q(othernames__icontains=othernames)

    phonenumber_1 = query_params.get('phonenumber_1')
    if phonenumber_1:
        filters &= Q(phonenumber_1=phonenumber_1)

    phonenumber_2 = query_params.get('phonenumber_2')
    if phonenumber_2:
        filters &= Q(phonenumber_2=phonenumber_2)

    email = query_params.get('email')
    if email:
        filters &= Q(email__icontains=email)

    address = query_params.get('address')
    if address:
        filters &= Q(address__icontains=address)

    customers = Customer.objects.filter(filters)
    serializer = CustomerSerializer(customers, many=True)

    return create_standard_response(
        status=status.HTTP_200_OK,
        message="Customer search results retrieved successfully",
        data=serializer.data
    )

