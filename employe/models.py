from django.db import models

# Create your models here.
class Emp(models.Model):
    name=models.CharField(max_length=200)
    emp_id=models.CharField(max_length=200)
    phone=models.BigIntegerField()
    address=models.CharField(max_length=200)
    working=models.BooleanField(default=True)
    department=models.CharField(max_length=20)

    def __str__(self):
        return self.name
    

# Create your models here.
class Userlogin(models.Model):
    username=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    email=models.EmailField(blank=False)
    islogin=models.CharField(max_length=200)

    def __str__(self):
        return self.username
    
    # Create your models here.
class Contactus(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField(blank=False)
    message=models.CharField(max_length=20)
    

    def __str__(self):
        return self.name
    