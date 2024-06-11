from django_filters import rest_framework as filters
from . import models


# class CustomerFilter(filters.FilterSet):
#     class Meta:
#         model = models.Customer
#         fields = {
#             'firstname': ['icontains'],
#             'othernames': ['icontains'],
#             'phonenumber_1': ['exact'],
#             'phonenumber_2': ['exact'],
#             'email': ['icontains'],
#             'address': ['icontains']
#         }