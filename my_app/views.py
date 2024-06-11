from .auth_views import signup, login
from .consultation_views import add_consultation_fee
from .customer_views import add_customer, edit_customer, delete_customer, search_customers, get_customer
from .employer_company_views import add_employer_company, edit_employer_company, delete_employer_company, search_employer_company, get_employer_company
from .job_position_views import add_jobposition, edit_jobposition, delete_jobposition, search_jobpositions, get_jobposition
from .job_views import add_job, edit_job, delete_job, search_jobs, get_job
from .payments import add_fee_payment
from .placements import add_placement, edit_placement, delete_placement, search_placement, get_placement
from .registration_fee_views import add_registration_fee
from .settings_views import add_settings, edit_settings, company_settings_view
# from .conn
