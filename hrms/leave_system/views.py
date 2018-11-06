import json
import re
from django.db.models import Q
from collections import OrderDict
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import get_user_model

from django.views.generic import View,TemplateView, DetailsView,
from django.db.models import Count
from .models import LeaveCategory,EmployeeLeaveProfile,LeaveApplication
# Create your views here.


