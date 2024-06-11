from django.urls import path
from . import views


urlpatterns = [

    # urls for authentication
    path("signup/", views.signup, name="signup"),
    path("login/", views.login, name="login"),

    # urls for settings 
    path("settings/", views.company_settings_view, name="company_settings_view"),

    # urls for customers
    path('customers/', views.add_customer, name='add_customer'),
    path('edit_customer/<int:pk>/', views.edit_customer, name='edit_customer'),
    path('customers/<int:pk>/delete/', views.delete_customer, name='delete_customer'),
    path('customers/<int:pk>/', views.get_customer, name='get_customer'),
    path('customers/search/', views.search_customers, name='customer_search'),

    # urls for jobs
    path('jobs/', views.add_job, name='add_job'),
    path('edit_job/<int:pk>/', views.edit_job, name='edit_job'),
    path('jobs/<int:pk>/delete/', views.delete_job, name='delete_job'),
    path('jobs/<int:pk>/', views.get_job, name='get_job'),
    path('jobs/search/', views.search_jobs, name='job_search'),

    # urls for jobpositions
    path('jobpositions/', views.add_jobposition, name='add_jobposition'),
    path('edit_jobposition/<int:pk>/', views.edit_jobposition, name='edit_jobposition'),
    path('jobpositions/<int:pk>/delete/', views.delete_jobposition, name='delete_jobposition'),
    path('jobpositions/<int:pk>/', views.get_jobposition, name='get_jobposition'),
    path('jobpositions/search/', views.search_jobpositions, name='jobposition_search'),

    # urls for employer_companies
    path('employer_companies/', views.add_employer_company, name='add_employer_company'),
    path('edit_employer_company/<int:pk>/', views.edit_employer_company, name='edit_employer_company'),
    path('employer_companies/<int:pk>/delete/', views.delete_employer_company, name='delete_employer_company'),
    path('employer_companies/<int:pk>/', views.get_employer_company, name='get_employer_company'),
    path('employer_companies/search/', views.search_employer_company, name='employer_company_search'),

    # urls for making placements
    path('placements/', views.add_placement, name='add_placement'),
    path('edit_placement/<int:pk>/', views.edit_placement, name='edit_placement'),
    path('placements/<int:pk>/delete/', views.delete_placement, name='delete_placement'),
    path('placements/<int:pk>/', views.get_placement, name='get_placement'),
    path('placements/search/', views.search_placement, name='placement_search'),

    # urls for managing connection fees
    # path('add-connection-fee/', views.add_connection_fee, name='add-connection-fee'),
    # path('edit_placement/<int:pk>/', views.edit_placement, name='edit_placement'),
    # path('placements/<int:pk>/delete/', views.delete_placement, name='delete_placement'),
    # path('placements/<int:pk>/', views.get_placement, name='get_placement'),
    # path('placements/search/', views.search_placement, name='placement_search'),

    # urls for managing connection fees
    path('add-fee-payment/', views.add_fee_payment, name='add-fee-payment'),

    # urls for managing registration fees
    path('add-registration-fee/', views.add_registration_fee, name='add-registration-fee'),

    # urls for managing registration fees
    path('add-consultation-fee/', views.add_consultation_fee, name='add-consultation-fee'),
]