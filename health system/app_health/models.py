from django.db import models

# Create your models here.

class User(models.Model):
    fullname=models.CharField(max_length=50)
    username=models.EmailField(unique=True)
    password=models.CharField(max_length=50)
    profilepic = models.FileField(upload_to='media/',default="anonymous.jpg")
    contact=models.CharField(max_length=10)
    def __str__(self):
        return self.fullname
    
class doctor_User(models.Model):
    doctorname=models.CharField(max_length=50)
    specializations=models.CharField(max_length=50)
    doctorpic=models.FileField(upload_to='media/',default="anonymous.jpg")
    contact=models.CharField(max_length=10)
    desc=models.CharField(max_length=1500)
    disease=models.CharField(max_length=50)

    def __str__(self):
        return self.doctorname
    
class disease_User(models.Model):
    doctor=models.CharField(max_length=50)
    diseasename=models.CharField(max_length=50)
    symptoms=models.CharField(max_length=100)
    precaution=models.CharField(max_length=500)
    medicinename=models.CharField(max_length=50)
    descpic=models.FileField(upload_to='media/',default="anonymous.jpg")
    productname=models.CharField(max_length=30,default=0)

    def __str__(self):
        return self.diseasename
    
class medicine_User(models.Model):
    diseasename=models.CharField(max_length=50)
    medicinename=models.CharField(max_length=50)
    medprecaution=models.CharField(max_length=100)
    meddesc=models.CharField(max_length=100)
    medprice=models.CharField(max_length=10)

    def __str__(self):
        return self.medicinename

class product_User(models.Model):
    productname=models.CharField(max_length=30)
    productprice=models.CharField(max_length=10)
    productdesc=models.CharField(max_length=200,default=0)
    productbenefit=models.CharField(max_length=200,default=0)
    productqty=models.CharField(max_length=10,default=0)

    def __str__(self):
        return self.productname
