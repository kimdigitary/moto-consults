# Generated by Django 5.0.6 on 2024-06-11 20:05

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanySettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=64)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='logos/')),
                ('favicon', models.ImageField(blank=True, null=True, upload_to='favicons/')),
                ('address', models.CharField(max_length=64)),
                ('phone_number', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='ConsultationFees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fees_name', models.CharField(max_length=64)),
                ('fees_amount', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('othernames', models.CharField(max_length=100, null=True)),
                ('phonenumber_1', models.CharField(max_length=15)),
                ('phonenumber_2', models.CharField(blank=True, max_length=15, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('address', models.CharField(max_length=64)),
                ('passport_photo', models.ImageField(upload_to='passport_photos/')),
                ('file_upload', models.FileField(upload_to='uploaded_files/')),
                ('remarks', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='EmployerCompany',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=64)),
                ('address', models.CharField(max_length=64)),
                ('phone_number', models.CharField(max_length=15)),
                ('description', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='JobPosition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_position', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='ConnectionFees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fees_name', models.CharField(max_length=64)),
                ('fees_amount', models.IntegerField()),
                ('fees_status', models.CharField(choices=[('paid', 'Paid'), ('not_paid', 'Not Paid')], default='not_paid', max_length=20)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='FeesPayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fee_type', models.CharField(choices=[('registration', 'Registration Fee'), ('consultation', 'Consultation Fee')], max_length=20)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('payment_status', models.CharField(choices=[('unpaid', 'Unpaid'), ('paid', 'Paid'), ('partially_paid', 'Partially Paid')], default='unpaid', max_length=20)),
                ('payment_date', models.DateTimeField(auto_now_add=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_app.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(max_length=64)),
                ('job_field', models.CharField(blank=True, max_length=64, null=True)),
                ('job_description', models.TextField(blank=True, null=True)),
                ('job_company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='my_app.employercompany')),
                ('job_position', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='my_app.jobposition')),
            ],
        ),
        migrations.CreateModel(
            name='Payments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_app.customer')),
            ],
        ),
        migrations.CreateModel(
            name='RecruitmentProcess',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('applied', 'Applied'), ('pending', 'Pending'), ('interviewed', 'Interviewed'), ('not_hired', 'Not Hired'), ('hired', 'Hired'), ('rejected_offer', 'Rejected the Offer')], default='applied', max_length=64)),
                ('application_date', models.DateTimeField(auto_now_add=True)),
                ('expected_salary', models.IntegerField(default=0)),
                ('connection_fee', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='my_app.connectionfees')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_app.customer')),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_app.job')),
            ],
        ),
        migrations.CreateModel(
            name='RegistrationFees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fees_name', models.CharField(max_length=64)),
                ('fees_amount', models.IntegerField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddConstraint(
            model_name='feespayment',
            constraint=models.UniqueConstraint(fields=('customer', 'fee_type'), name='unique_customer_fees'),
        ),
    ]