# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-29 05:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0001_initial'),
        ('customers', '0003_customer_number_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='emp_department',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Employee Wroking Department'),
        ),
        migrations.AddField(
            model_name='customer',
            name='employees',
            field=models.ManyToManyField(help_text='Employess working with customer', to='people.Employee', verbose_name='Employees'),
        ),
        migrations.AddField(
            model_name='customer',
            name='num_employess',
            field=models.CharField(blank=True, help_text='Our emplooyes number with customer', max_length=2, null=True, verbose_name='Number of Employees'),
        ),
        migrations.AddField(
            model_name='customer',
            name='onsite_deliver',
            field=models.BooleanField(default=True, verbose_name='Onsite Deliver'),
        ),
    ]