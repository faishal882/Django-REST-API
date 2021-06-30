from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from EmployeeApp.models import Departments, Employee
from EmployeeApp.serializers import DepartmentSerializer, EmployeeSerializer

from django.core.files.storage import default_storage

# Create your views here.
@csrf_exempt
def departmentApi(request,id=0):
 if request.method == 'GET':
  departments = Departments.objects.all()
  departments_serializer = DepartmentSerializer(departments, many=True)
  return JsonResponse(departments_serializer.data, safe=False)

 elif request.method == 'POST':
  department_data = JSONParser().parse(request)
  department_serializer = DepartmentSerializer(data=department_data)
  if department_serializer.is_valid():
   department_serializer.save()
   return JsonResponse("Added Succesfully!!!", safe=False)
  return JsonResponse("Failed to Add.", safe=False)

 elif request.method == 'PUT':
  department_data = JSONParser().parse(request)
  department = Departments.objects.get(DepartmentId = department_data['DepartmentId'])
  department_serializer = DepartmentSerializer(department, data=department_data)
  if department_serializer.is_valid():
   department_serializer.save()
   return JsonResponse("Updated Sucessfully!!!", safe=False)
  return JsonResponse("Failed to Update", safe=False)

 elif request.method == 'DELETE':
  department = Departments.objects.get(DepartmentId = id)
  department.delete()
  return JsonResponse("Deleted Sucessfully!!!", safe=False)


@csrf_exempt
def employeeApi(request,id=0):
 if request.method == 'GET':
  employees = Employee.objects.all()
  employees_serializer = EmployeeSerializer(employees, many=True)
  return JsonResponse(employees_serializer.data, safe=False)

 elif request.method == 'POST':
  employees_data = JSONParser().parse(request)
  employees_serializer = EmployeeSerializer(data = employees_data)
  if employees_serializer.is_valid():
   employees_serializer.save()
   return JsonResponse("Added Succesfully!!!", safe=False)
  return JsonResponse("Failed to Add.", safe=False)

 elif request.method == 'PUT':
  employees_data = JSONParser().parse(request)
  employees = Employee.objects.get(EmployeeId = employees_data['EmployeeId'])
  employees_serializer = EmployeeSerializer(employees, data=employees_data)
  if employees_serializer.is_valid():
   employees_serializer.save()
   return JsonResponse("Updated Sucessfully!!!", safe=False)
  return JsonResponse("Failed to Update", safe=False)

 elif request.method == 'DELETE':
  employees = Employee.objects.get(EmployeeId = id)
  employees.delete()
  return JsonResponse("Deleted Sucessfully!!!", safe=False)


@csrf_exempt
def SaveFile(request):
 file = request.FILES['myFile']
 file_name = default_storage.save(file.name, file)

 return JsonResponse(file_name, safe=False)