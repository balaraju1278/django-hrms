# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2018-10-24 10:57
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('DATA SCIENCE', 'DATA SCIENCE'), ('PRODUCTS', 'PRODUCTS'), ('OPERATIONS', 'OPERATIONS'), ('ADMIN', 'ADMIN')], max_length=50, unique=True, verbose_name='Department Name')),
                ('code', models.CharField(max_length=10, unique=True, verbose_name='Department Code')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Department',
                'verbose_name': 'Department',
            },
        ),
        migrations.CreateModel(
            name='EmpBankInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bank_account_number', models.PositiveIntegerField(blank=True, null=True, unique=True, validators=[django.core.validators.MinValueValidator(10000000), django.core.validators.MaxValueValidator(99999999)], verbose_name='Bank Account Number')),
                ('ifsc_code', models.CharField(blank=True, max_length=50, null=True, verbose_name='Bank IFSC Code')),
                ('bank_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='Bank Name')),
                ('pan_num', models.CharField(blank=True, max_length=50, null=True, unique=True, verbose_name='PAN ID')),
            ],
            options={
                'verbose_name_plural': 'Employees Bank Details',
                'verbose_name': 'Employees Bank Details',
            },
        ),
        migrations.CreateModel(
            name='EmpContactInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_email', models.EmailField(blank=True, max_length=100, null=True, unique=True, verbose_name='Contact Email')),
                ('contact_number', models.CharField(blank=True, max_length=10, null=True, unique=True, verbose_name='Contact Number')),
                ('linkedin', models.CharField(blank=True, max_length=150, null=True, unique=True, verbose_name='LinkedIn ID')),
                ('github', models.CharField(blank=True, max_length=150, null=True, unique=True, verbose_name='Github ID')),
                ('facebook', models.CharField(blank=True, max_length=150, null=True, unique=True, verbose_name='Facebook')),
                ('blog', models.CharField(blank=True, max_length=150, null=True, unique=True, verbose_name='Personal Blog')),
            ],
            options={
                'verbose_name_plural': 'Employees Contact Information',
                'verbose_name': 'Employees Contact Information',
            },
        ),
        migrations.CreateModel(
            name='EmpDesignation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Designation')),
                ('code', models.CharField(max_length=10, verbose_name='Department Code')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='people.Department', verbose_name='Department')),
            ],
            options={
                'verbose_name_plural': 'Designation',
                'verbose_name': 'Designtion',
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=100, null=True, validators=[django.core.validators.RegexValidator(code='invalid_full_name', message='Name must be Alphabetic', regex='^[a-zA-Z]*$')], verbose_name='First Name')),
                ('last_name', models.CharField(blank=True, max_length=100, null=True, validators=[django.core.validators.RegexValidator(code='invalid_full_name', message='Name must be Alphabetic', regex='^[a-zA-Z]*$')], verbose_name='Last Name')),
                ('pref_name', models.CharField(blank=True, max_length=100, null=True, validators=[django.core.validators.RegexValidator(code='invalid_full_name', message='Name must be Alphabetic', regex='^[a-zA-Z]*$')], verbose_name='Prefer Name')),
                ('gender', models.CharField(choices=[('M', 'Male'), ('FM', 'Female')], max_length=2, verbose_name='Gender')),
                ('date_of_birth', models.DateTimeField(blank=True, null=True, verbose_name='Date of Birth')),
                ('marital_status', models.CharField(choices=[('MR', 'MARRIED'), ('S', 'SINGLE')], default='S', max_length=2, verbose_name='Marital Status')),
                ('emp_code', models.CharField(blank=True, max_length=10, null=True, unique=True, verbose_name='Employee ID')),
                ('company_email', models.EmailField(blank=True, max_length=100, null=True, unique=True, verbose_name='Company Email')),
                ('picture', models.ImageField(blank=True, height_field='height_field', null=True, upload_to='', width_field='width_field')),
                ('height_field', models.IntegerField(default=600, null=True)),
                ('width_field', models.IntegerField(default=600, null=True)),
                ('joined_date', models.DateField(blank=True, verbose_name='Joined Data')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='people.Department', verbose_name='Department')),
            ],
            options={
                'verbose_name_plural': 'Employees',
                'verbose_name': 'Employee',
            },
        ),
        migrations.CreateModel(
            name='EmpMailingAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('door_num', models.CharField(blank=True, max_length=6, null=True, verbose_name='Door Number')),
                ('street', models.CharField(blank=True, max_length=15, null=True, verbose_name='Street Name')),
                ('city', models.CharField(blank=True, max_length=40, null=True, validators=[django.core.validators.RegexValidator(code='invalid_full_name', message='Name must be Alphabetic', regex='^[a-zA-Z]*$')], verbose_name='City')),
                ('state', models.CharField(blank=True, max_length=50, null=True, validators=[django.core.validators.RegexValidator(code='invalid_full_name', message='Name must be Alphabetic', regex='^[a-zA-Z]*$')], verbose_name='State')),
                ('country', models.CharField(blank=True, max_length=50, null=True, validators=[django.core.validators.RegexValidator(code='invalid_full_name', message='Name must be Alphabetic', regex='^[a-zA-Z]*$')], verbose_name='Country')),
                ('pincode', models.CharField(blank=True, max_length=6, null=True, verbose_name='Pincode')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='people.Employee', verbose_name='Employee')),
            ],
            options={
                'verbose_name_plural': 'Employee Mailing Address',
                'verbose_name': 'Employee Mailing Address',
            },
        ),
        migrations.AddField(
            model_name='empdesignation',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='people.Employee', verbose_name='Employee'),
        ),
        migrations.AddField(
            model_name='empcontactinfo',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='people.Employee', verbose_name='Employee'),
        ),
        migrations.AddField(
            model_name='empbankinfo',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='people.Employee', verbose_name='Employee'),
        ),
    ]