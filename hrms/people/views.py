from django.shortcuts import render


from people.models import (Department,
                           Employee,
                           EmpDesignation,
                           EmpContactInfo,
                           EmpMailingAddress,
                           EmpBankInfo,
                           EmpSkillProfile)
# Create your views here.


def add_department(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        code = request.POST.get('code')
        department_head = request.POST.get('department_head')
        department_head_mail = request.POST.get('department_head_mail')
        dpmnt = Department()
        dpmnt.name = name
        dpmnt.code = code
        dpmnt.department_head = department_head
        dpmnt.department_head_mail = department_head_mail
        dpmnt.save()
        return HttpResponse(dpmnt.id)
        

def edit_department():
    pass


def delete_department():
    pass

def add_employee():
    pass


def edit_employee():
    pass


def delete_employee():
    pass


def add_employee_bank_info():
    pass


def edit_employee_bank_info():
    pass


def delete_employee_bank_info():
    pass    


def add_emp_skill_profile():
    pass


def edit_emp_skill_profile():
    pass


def delete_emp_skill_profile():
    pass


def add_emp_mailing_address():
    pass


def edit_emp_mailing_address():
    pass


def delete_emp_mailing_address():
    pass


def add_emp_designation():
    pass


def edit_emp_designation():
    pass


def delete_emp_designation():
    pass


class EmployeeDetails():
    pass


class DepartmentDetails():
    pass



class EmployeesHomeView():
    pass
