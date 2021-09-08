from django.db import models

# Create your models here.
# ID, Name, Age, Sex, Father Name, Mother Name, Last Education
class User(models.Model):
    S_id = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    sex = models.CharField(max_length=10)
    father_name = models.CharField(max_length=100)
    mother_name = models.CharField(max_length=100)
    last_education = models.CharField(max_length=100)

    # def __str__(self):
    #     return self.name