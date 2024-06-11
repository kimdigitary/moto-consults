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



# DEALING WITH CONSULTATION FEES 
@api_view(['POST'])
def add_consultation_fee(request):
    if request.method == 'POST':
        serializer = ConsultationFeesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return create_standard_response(status=status.HTTP_201_CREATED, message="Consultation fee created successfully", data=serializer.data)
        return create_standard_response(status=status.HTTP_400_BAD_REQUEST, message="Failed to create consultation fee", data=serializer.errors)
    

