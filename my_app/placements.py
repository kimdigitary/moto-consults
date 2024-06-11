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




# DEALING WITH RECRUITMENT PROCESS / PLACEMENTS
@api_view(['POST'])
def add_placement(request):
    if request.method == 'POST':
        serializer = RecruitmentProcessSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return create_standard_response(status=status.HTTP_201_CREATED, message="placement created successfully", data=serializer.data)
        return create_standard_response(status=status.HTTP_400_BAD_REQUEST, message="Failed to create new placement", data=serializer.errors)


@api_view(['GET', 'PUT'])
def edit_placement(request, pk):
    try:
        placement = RecruitmentProcess.objects.get(pk=pk)
    except RecruitmentProcess.DoesNotExist:
        return create_standard_response(status=status.HTTP_404_NOT_FOUND, message="placement not found")

    if request.method == 'GET':
        serializer = RecruitmentProcessSerializer(placement)
        return create_standard_response(status=status.HTTP_200_OK, message="Placement details retrieved successfully", data=serializer.data)

    elif request.method == 'PUT':
        serializer = RecruitmentProcessSerializer(placement, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return create_standard_response(status=status.HTTP_200_OK, message="Employer company updated successfully", data=serializer.data)
        return create_standard_response(status=status.HTTP_400_BAD_REQUEST, message="Failed to update Employer company details", data=serializer.errors)


@api_view(['DELETE'])
def delete_placement(request, pk):
    try:
        placement = RecruitmentProcess.objects.get(pk=pk)
    except RecruitmentProcess.DoesNotExist:
        return create_standard_response(status=status.HTTP_404_NOT_FOUND, message="Placement not found")

    if request.method == 'DELETE':
        placement.delete()
        return create_standard_response(status=status.HTTP_204_NO_CONTENT, message="Placement deleted successfully")


@api_view(['GET'])
def get_placement(request, pk):
    try:
        placement = RecruitmentProcess.objects.get(pk=pk)
    except RecruitmentProcess.DoesNotExist:
        return create_standard_response(status=status.HTTP_404_NOT_FOUND, message="Placement not found")

    if request.method == 'GET':
        serializer = RecruitmentProcessSerializer(placement)
        return create_standard_response(status=status.HTTP_200_OK, message="Placement details retrieved successfully", data=serializer.data)
    

# @api_view(['GET'])
# def search_placement(request):
#     query_params = request.query_params
#     filters = Q()

#     customer = query_params.get('customer')
#     if customer:
#         filters &= (Q(customer__firstname__icontains=customer) | 
#                     Q(customer__othernames__icontains=customer) | 
#                     Q(customer__email__icontains=customer) | 
#                     Q(customer__phonenumber_1__icontains=customer) | 
#                     Q(customer__phonenumber_2__icontains=customer))

#     job = query_params.get('job')
#     if job:
#         filters &= (Q(job__job_title__icontains=job) | 
#                     Q(job__job_field__icontains=job) | 
#                     Q(job__job_description__icontains=job) | 
#                     Q(job__job_company__name__icontains=job))

#     status = query_params.get('status')
#     if status:
#         filters &= Q(status__icontains=status)

#     placements = RecruitmentProcess.objects.filter(filters)
#     serializer = RecruitmentProcessSerializer(placements, many=True)

#     return Response(
#         data={
#             'status': status.HTTP_200_OK,
#             'message': "Placement search results retrieved successfully",
#             'data': serializer.data
#         },
#         status=status.HTTP_200_OK
#     )

 
@api_view(['GET'])
def search_placement(request):
    query_params = request.query_params
    filters = Q()

    customer = query_params.get('customer')
    if customer:
        filters &= (Q(customer__firstname__icontains=customer) | 
                    Q(customer__othernames__icontains=customer) | 
                    Q(customer__email__icontains=customer) | 
                    Q(customer__phonenumber_1__icontains=customer) | 
                    Q(customer__phonenumber_2__icontains=customer))

    job = query_params.get('job')
    if job:
        filters &= (Q(job__job_title__icontains=job) | 
                    Q(job__job_field__icontains=job) | 
                    Q(job__job_description__icontains=job) | 
                    Q(job__job_company__name__icontains=job))

    # status = query_params.get('status')
    # if status:
    #     filters &= Q(status__icontains=status)

    # placements = RecruitmentProcess.objects.filter(filters)
    # serializer = RecruitmentProcessSerializer(placements, many=True)

    # return create_standard_response(
    #     status=status.HTTP_200_OK,
    #     message="Customer search results retrieved successfully",
    #     data=serializer.data
    # )
    status_param = query_params.get('status')
    if status_param:
        filters &= Q(status__icontains=status_param)

    placements = RecruitmentProcess.objects.filter(filters)
    serializer = RecruitmentProcessSerializer(placements, many=True)

    return create_standard_response(
        status=status.HTTP_200_OK,
        message="Customer search results retrieved successfully",
        data=serializer.data
    )

