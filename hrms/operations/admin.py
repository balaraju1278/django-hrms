from django.contrib import admin
from django.db import models
from .scheduler.base import PhoneAddress, EmailAddress, Person
from .scheduler.call import Call,InvestorCall,InterviewCall,CustomerCall
from .scheduler.out_visit import EmployeeVisit
from .scheduler.visit import CustomerVisit
from .scheduler.placement_drive import RecruitmentDrive
from .scheduler.event import BaseEvent,Outing,Conference,Hackathon, TeamLunch
from .scheduler.board_meeting import BoardMeeting


# Register your models here.

admin.site.register(PhoneAddress)
admin.site.register(EmailAddress)
admin.site.register(Call)
admin.site.register(InvestorCall)
admin.site.register(InterviewCall)
admin.site.register(CustomerCall)
admin.site.register(EmployeeVisit)
admin.site.register(CustomerVisit)
admin.site.register(RecruitmentDrive)

admin.site.register(BaseEvent)
admin.site.register(Outing)
admin.site.register(Conference)
admin.site.register(Hackathon)
admin.site.register(TeamLunch)

admin.site.register(BoardMeeting)