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




# DEALING WITH JOBS 
@api_view(['POST'])
def add_job(request):
    if request.method == 'POST':
        serializer = JobSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return create_standard_response(status=status.HTTP_201_CREATED, message="Job created successfully", data=serializer.data)
        return create_standard_response(status=status.HTTP_400_BAD_REQUEST, message="Failed to create new job", data=serializer.errors)


@api_view(['GET', 'PUT'])
def edit_job(request, pk):
    try:
        job = Job.objects.get(pk=pk)
    except job.DoesNotExist:
        return create_standard_response(status=status.HTTP_404_NOT_FOUND, message="Job not found")

    if request.method == 'GET':
        serializer = JobSerializer(job)
        return create_standard_response(status=status.HTTP_200_OK, message="Job details retrieved successfully", data=serializer.data)

    elif request.method == 'PUT':
        serializer = JobSerializer(job, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return create_standard_response(status=status.HTTP_200_OK, message="Job updated successfully", data=serializer.data)
        return create_standard_response(status=status.HTTP_400_BAD_REQUEST, message="Failed to update job details", data=serializer.errors)


@api_view(['DELETE'])
def delete_job(request, pk):
    try:
        job = Job.objects.get(pk=pk)
    except job.DoesNotExist:
        return create_standard_response(status=status.HTTP_404_NOT_FOUND, message="Job not found")

    if request.method == 'DELETE':
        job.delete()
        return create_standard_response(status=status.HTTP_204_NO_CONTENT, message="Job deleted successfully")


@api_view(['GET'])
def get_job(request, pk):
    try:
        job = Job.objects.get(pk=pk)
    except Job.DoesNotExist:
        return create_standard_response(status=status.HTTP_404_NOT_FOUND, message="Job not found")

    if request.method == 'GET':
        serializer = JobSerializer(job)
        return create_standard_response(status=status.HTTP_200_OK, message="Job details retrieved successfully", data=serializer.data)
    

@api_view(['GET'])
def search_jobs(request):
    query_params = request.query_params
    filters = Q()

    job_title = query_params.get('job_title')
    if job_title:
        filters &= Q(job_title__icontains=job_title)

    job_field = query_params.get('job_field')
    if job_field:
        filters &= Q(job_field__icontains=job_field)

    jobs = Job.objects.filter(filters)
    serializer = JobSerializer(jobs, many=True)

    return create_standard_response(
        status=status.HTTP_200_OK,
        message="Job search results retrieved successfully",
        data=serializer.data
    )



