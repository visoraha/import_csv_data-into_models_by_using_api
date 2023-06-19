from django.db import models

# Create your models here.

class Bank(models.Model):
    bname=models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.bname

class Branch(models.Model):
    bname=models.ForeignKey(Bank,on_delete=models.CASCADE)
    IFSC=models.CharField(max_length=20,primary_key=True)
    branch=models.CharField(max_length=80)
    address=models.TextField()
    contact=models.IntegerField(max_length=10)
    city=models.CharField(max_length=40)
    district=models.CharField(max_length=60)
    state=models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.city
