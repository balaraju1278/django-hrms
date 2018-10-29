from django.db import models
from .scheduler.base import PhoneAddress, EmailAddress, Person
from .scheduler.call import Call,InvestorCall,InterviewCall,CustomerCall
from .scheduler.out_visit import EmployeeVisit
from .scheduler.visit import CustomerVisit
from .scheduler.placement_drive import RecruitmentDrive
from .scheduler.board_meeting import BoardMeeting
from .scheduler.event import BaseEvent,Outing,Conference,Hackathon, TeamLunch
# Create your models here.
