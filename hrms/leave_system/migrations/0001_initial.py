# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-29 04:22
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('people', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeLeaveProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_leaves', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(99999999999)])),
                ('employee', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='people.Employee', verbose_name='Empplooye')),
            ],
            options={
                'verbose_name_plural': 'Employee Leave Profiles',
                'verbose_name': 'Employee Leave Profiles',
            },
        ),
        migrations.CreateModel(
            name='LeaveApplication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('num_of_days', models.IntegerField()),
                ('status', models.BooleanField(default=False)),
                ('subject', models.CharField(max_length=500)),
                ('body', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='LeaveCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_of_leave', models.CharField(blank=True, choices=[('CL', 'Casual Leave'), ('ML', 'Medical Leave'), ('WH', 'Work From Homw')], max_length=25, null=True, verbose_name='Leave Type')),
                ('number_of_days', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(9999999999)])),
            ],
            options={
                'verbose_name_plural': 'Leave Categories',
                'verbose_name': 'Leave Categories',
            },
        ),
        migrations.AddField(
            model_name='leaveapplication',
            name='leave_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='leave_system.LeaveCategory'),
        ),
    ]