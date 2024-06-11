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




# DEALING WITH JOBPOSITIONS 
@api_view(['POST'])
def add_jobposition(request):
    if request.method == 'POST':
        serializer = JobPositionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return create_standard_response(status=status.HTTP_201_CREATED, message="Jobposition created successfully", data=serializer.data)
        return create_standard_response(status=status.HTTP_400_BAD_REQUEST, message="Failed to create new jobposition", data=serializer.errors)


@api_view(['GET', 'PUT'])
def edit_jobposition(request, pk):
    try:
        jobposition = JobPosition.objects.get(pk=pk)
    except JobPosition.DoesNotExist:
        return create_standard_response(status=status.HTTP_404_NOT_FOUND, message="Job position not found")

    if request.method == 'GET':
        serializer = JobPositionSerializer(jobposition)
        return create_standard_response(status=status.HTTP_200_OK, message="Job position details retrieved successfully", data=serializer.data)

    elif request.method == 'PUT':
        serializer = JobPositionSerializer(jobposition, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return create_standard_response(status=status.HTTP_200_OK, message="Job position updated successfully", data=serializer.data)
        return create_standard_response(status=status.HTTP_400_BAD_REQUEST, message="Failed to update job position details", data=serializer.errors)


@api_view(['DELETE'])
def delete_jobposition(request, pk):
    try:
        jobposition = JobPosition.objects.get(pk=pk)
    except JobPosition.DoesNotExist:
        return create_standard_response(status=status.HTTP_404_NOT_FOUND, message="Job position not found")

    if request.method == 'DELETE':
        jobposition.delete()
        return create_standard_response(status=status.HTTP_204_NO_CONTENT, message="Job position deleted successfully")


@api_view(['GET'])
def get_jobposition(request, pk):
    try:
        jobposition = JobPosition.objects.get(pk=pk)
    except JobPosition.DoesNotExist:
        return create_standard_response(status=status.HTTP_404_NOT_FOUND, message="Job position not found")

    if request.method == 'GET':
        serializer = JobPositionSerializer(jobposition)
        return create_standard_response(status=status.HTTP_200_OK, message="Job position details retrieved successfully", data=serializer.data)
    

@api_view(['GET'])
def search_jobpositions(request):
    query_params = request.query_params
    filters = Q()

    job_position = query_params.get('job_position')
    if job_position:
        filters &= Q(job_position__icontains=job_position)

    jobpositions = JobPosition.objects.filter(filters)
    serializer = JobPositionSerializer(jobpositions, many=True)

    return create_standard_response(
        status=status.HTTP_200_OK,
        message="Job position search results retrieved successfully",
        data=serializer.data
    )

