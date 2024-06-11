from django.contrib import admin
from . import models

# admin.site.register(models.UploadFile)
admin.site.register(models.Customer)
admin.site.register(models.Job)
admin.site.register(models.JobPosition)
admin.site.register(models.EmployerCompany)
admin.site.register(models.RecruitmentProcess)
admin.site.register(models.ConnectionFees)
admin.site.register(models.FeesPayment)
admin.site.register(models.CompanySettings)
admin.site.register(models.ConsultationFees)
admin.site.register(models.Payments)
admin.site.register(models.RegistrationFees)