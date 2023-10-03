from django.db import models

# Create your models here.
Department_list = [
    ("CS", "Computer Science"),
    ("MT", "Management Technology"),
    ("CSE","Computer Science Edu")
]



class MatricNumber(models.Model):
    

    first_name = models.CharField(max_length=50)
    Last_name = models.CharField(max_length=50)
    
    level = models.IntegerField()

    matricnumber = models.IntegerField()
        
    school_mail = models.EmailField()

    def __str__(self) -> str:
         return str(self.matricnumber)
    pass

class Department(models.Model):

    Department_list = [
        ("CS", "Computer Science"),
        ("MT", "Management Science"),
        ("CSE","Computer Science Edu")
]
    
    Department = models.CharField(max_length=50,choices=Department_list) 
    MatricNumber = models.ForeignKey(MatricNumber,on_delete = models.CASCADE)


class HashedPasword(models.Model):
        password = models.CharField(max_length=256)
        MatricNumber = models.ForeignKey(MatricNumber,on_delete=models.CASCADE)
