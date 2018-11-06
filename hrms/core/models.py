from people.models import (Department,
                           Employee,
                           EmpDesignation,
                           EmpContactInfo,
                           EmpMailingAddress,
                           EmpBankInfo,
                           EmpSkillProfile)
                           
from operations.scheduler.base import PhoneAddress, EmailAddress, Person
from operations.scheduler.call import Call,InvestorCall,InterviewCall,CustomerCall
from operations.scheduler.out_visit import EmployeeVisit
from operations.scheduler.visit import CustomerVisit
from operations.scheduler.placement_drive import RecruitmentDrive
from operations.scheduler.board_meeting import BoardMeeting
from operations.scheduler.event import BaseEvent,Outing,Conference,Hackathon, TeamLunch

from customers.c_models.customer_project import CustomerProject
from customers.c_models.customer import Customer

from leave_system.models import LeaveCategory, EmployeeLeaveProfile, LeaveApplication
from tasks.models import BaseTask, DevelopmentTask, OperationTask
