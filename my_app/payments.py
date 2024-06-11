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



# DEALING WITH FEES PAYMENTS 
# @api_view(['POST'])
# def add_fee_payment(request):
#     fee_type = request.data.get('fee_type')
#     customer = request.data.get('customer')
    
#     # Retrieve the customer
#     try:
#         customer = Customer.objects.get(pk=customer)
#     except Customer.DoesNotExist:
#         return Response({'error': 'Customer not found'}, status=404)
    
#     # Determine the fee amount based on the selected fee type
#     if fee_type == 'registration':
#         fee_amount = RegistrationFees.objects.get(fees_name='test payment').fees_amount
#     elif fee_type == 'consultation':
#         fee_amount = ConsultationFees.objects.get(fees_name='test payment').fees_amount
#     else:
#         return Response({'error': 'Invalid fee type'}, status=400)
    
#     # Create the FeePayment instance with the determined amount
#     fee_payment = FeesPayment.objects.create(
#         customer=customer,
#         fee_type=fee_type,
#         amount=fee_amount,
#         payment_status='unpaid',
#     )
    
#     # Return the created FeePayment instance
#     serializer = FeesPaymentSerializer(fee_payment)
#     return create_standard_response(status=status.HTTP_201_CREATED, message="payment added successfully", data=serializer.data)

@api_view(['POST'])
def add_fee_payment(request):
    fee_type = request.data.get('fee_type')
    customer = request.data.get('customer')
    
    # Retrieve the customer
    try:
        customer = Customer.objects.get(pk=customer)
    except Customer.DoesNotExist:
        return Response({'error': 'Customer not found'}, status=404)
    
    # Check if a payment already exists for this customer and fee type
    existing_payment = FeesPayment.objects.filter(customer=customer, fee_type=fee_type).first()
    
    # If a payment exists, update it; otherwise, create a new one
    if existing_payment:
        # Update the existing payment
        existing_payment.amount = RegistrationFees.objects.get(fees_name='test payment').fees_amount
        existing_payment.payment_status = 'unpaid'
        existing_payment.save()
        serializer = FeesPaymentSerializer(existing_payment)
        return Response({"status": "updated", "data": serializer.data}, status=200)
    else:
        # Create a new payment
        fee_amount = RegistrationFees.objects.get(fees_name='test payment').fees_amount
        fee_payment = FeesPayment.objects.create(
            customer=customer,
            fee_type=fee_type,
            amount=fee_amount,
            payment_status='unpaid',
        )
        serializer = FeesPaymentSerializer(fee_payment)
        return create_standard_response(status=status.HTTP_201_CREATED, message="payment added successfully", data=serializer.data)

