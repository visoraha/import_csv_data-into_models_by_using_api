from django.shortcuts import render
from app.models import *
import csv
from rest_framework.response import Response
from django.http import HttpResponse

# Create your views here.
def bank_upload(request):
    a='C:\\Users\\vicky\\OneDrive\\Desktop\\74de6\\API\Scripts\\project6\\bank.csv'

    with open(a,'r') as file:
        csv_data=csv.reader(file)

        next(csv_data)

        for row in csv_data:
            bn=row[0].strip()
            instance=Bank(bname=bn)
            instance.save()
        return HttpResponse('successful')


def branch_upload(request):
    b = 'C:\\Users\\vicky\\OneDrive\\Desktop\\74de6\\API\Scripts\\project6\\branch1.csv'
    
    with open(b, 'r') as file:
        csv_data = csv.reader(file)
          # Skip the header row if it exists
        next(csv_data)
        i=1
        for row in csv_data:
              i+=1
              bname = row[0]
              print(row[0])
              bo = Bank.objects.filter(bname=bname)[0]
              instance = Branch(
                      bname=bo,            
                      
                      IFSC= row[1],
                      branch = row[2],
                      address =row[3],
                      contact=row[4],
                      city = row[5],
                      district = row[6],
                      state = row[7],)
                                  
              instance.save()


       

        return HttpResponse('successful')