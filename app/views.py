from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
# Create your views here.
def Insert_Topic(request):
    tn=input("Enter Topic_name :")
    to=Topic.objects.get_or_create(Topic_name=tn)[0]
    to.save()
    return HttpResponse('<center><h1>Data Inserted Successfully</h1></center>')

def Insert_Webpage(request):
    tn=input("Enter Topic_name :")
    to=Topic.objects.get_or_create(Topic_name=tn)[0]
    to.save()
    n=input('Enter Name :')
    u=input('Enter Url :')
    wo=Webpage.objects.get_or_create(Topic_name=to,Name=n,Url=u)[0]
    wo.save()
    return HttpResponse('<center><h1>Data Inserted Successfully</h1></center>')

def Insert_AR(request):
    tn=input("Enter Topic_name :")
    to=Topic.objects.get_or_create(Topic_name=tn)[0]
    to.save()
    n=input('Enter Name :')
    u=input('Enter Url :')
    wo=Webpage.objects.get_or_create(Topic_name=to,Name=n,Url=u)[0]
    wo.save()
    d=input('Enter Date :')
    a=input('Enter Author :')
    e=input('Enter Email: ')
    ao=AccessRecords.objects.get_or_create(Name=wo,Date=d,Author=a,Email=e)[0]
    ao.save()
    return HttpResponse('<center><h1>Data Inserted Successfully</h1></center>')


