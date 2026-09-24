from django.db import models

# Create your models here.
class StudentDetails(models.Model):
    stid=models.IntegerField(primary_key=True)
    st_name=models.CharField(max_length=30)
    program=models.CharField(max_length=15)
    st_cgpa=models.DecimalField(max_digits=4,decimal_places=2)
    st_city=models.CharField(max_length=20)

    def __str__(self):
        return self.st_name+"-"+self.program