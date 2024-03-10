from django.db import models

# Create your models here.
EMPLOYEE_CHOICES = (
    ("Development", "Development"),
    ("Testing", "Testing"),
    ("HR", "HR"),
)

class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile = models.CharField(max_length=15)
    department = models.CharField(choices=EMPLOYEE_CHOICES,default="HR")

    def __str__(self):
        return self.name

class Attendance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField()
    is_present = models.BooleanField(null=True,blank=True)

    def __str__(self):
        return str(self.employee)