from django.db import models

# Create your models here.
class Student(models.Model):
    student_no = models.AutoField(db_column='STUDENT_NO', primary_key=True)  # Field name made lowercase.
    student_name = models.TextField(db_column='STUDENT_NAME')  # Field name made lowercase.
    student_dob = models.DateField(db_column='STUDENT_DOB')  # Field name made lowercase.
    student_doj = models.DateField(db_column='STUDENT_DOJ')  # Field name made lowercase.
    
    class Meta:
        managed = False
        db_table = 'STUDENT'