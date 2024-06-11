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


@api_view(["POST"])
def login(request):
    user = get_object_or_404(User, username=request.data["username"])
    if not user.check_password(request.data["password"]):
        return Response({"detail": "User not found"}, status=status.HTTP_400_BAD_REQUEST)
    token, created = Token.objects.get_or_create(user=user)
    serializer = UserSerializer(instance=user)
    return Response({"token": token.key, "user": serializer.data})


# @api_view(["POST"])
# def signup(request):
#     serializer = UserSerializer(data=request.data)
#     if serializer.is_valid():
#         user = serializer.save()
#         user.set_password(request.data["password"])
#         user.save()
#         token, created = Token.objects.get_or_create(user=user)
#         return create_standard_response(status.HTTP_200_OK, "User created successfully.", {
#             "token": token.key,
#             "user": serializer.data
#         })
#     return create_standard_response(status.HTTP_400_BAD_REQUEST, "Invalid user details.", serializer.errors)

@api_view(['POST'])
def signup(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        user.set_password(request.data["password"])
        user.save()
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            "status": "success",
            "message": "User created successfully.",
            "data": {
                "token": token.key,
                "user": serializer.data
            }
        }, status=status.HTTP_201_CREATED)
    return Response({
        "status": "error",
        "message": "Invalid user details.",
        "errors": serializer.errors
    }, status=status.HTTP_400_BAD_REQUEST)