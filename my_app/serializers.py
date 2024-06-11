from rest_framework import serializers
from.models import Customer, CompanySettings, Job, JobPosition, CompanySettings, EmployerCompany, RecruitmentProcess, ConnectionFees, FeesPayment, RegistrationFees, ConsultationFees
from django.contrib.auth.models import User
from rest_framework.response import Response


def create_standard_response(status, message, data=None):
    """
    Creates a standardized response dictionary with status, message, and optional data.
    """
    response = {
        'status': status,
        'message': message,
    }
    if data is not None:
        response['data'] = data
    return Response(response)


# class UserSerializer(serializers.ModelSerializer):
#     class Meta(object):
#         model = User
#         fields = ["id", "username", "password", "email"]

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password", "email"]
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"


class CompanySettingsSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = CompanySettings
        fields = "__all__"


class JobSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Job 
        fields = "__all__"


class JobPositionSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = JobPosition 
        fields = "__all__"


class EmployerCompanySerializer(serializers.ModelSerializer):
    class Meta(object):
        model = EmployerCompany 
        fields = "__all__"


class RecruitmentProcessSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = RecruitmentProcess 
        fields = "__all__"



class ConnectionFeesSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = ConnectionFees 
        fields = "__all__"


class FeesPaymentSerializer(serializers.ModelSerializer):
    amount = serializers.DecimalField(max_digits=10, decimal_places=2, write_only=True)

    class Meta:
        model = FeesPayment
        fields = '__all__'


class RegistrationFeesSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistrationFees
        fields = ['fees_name', 'fees_amount']


class ConsultationFeesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConsultationFees
        fields = ['fees_name', 'fees_amount']