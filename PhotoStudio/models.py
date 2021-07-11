from django.db import models

# Create your models here.

class Appointments(models.Model):
    User_id = models.AutoField(primary_key=True)
    User_FirstName = models.CharField(max_length=20, default=' ')
    User_LastName = models.CharField(max_length=20, default=' ', null=True)
    User_Email = models.EmailField(max_length=30, null=True)
    User_Contact = models.CharField(max_length=10)
    User_BookedOn = models.DateField(default=' ')
    User_ApptDate = models.DateField(default=' ')
    User_Event = models.CharField(max_length=30, default='other')
    User_Suggestion = models.TextField(null=True)
    def __str__(self):
        return f"{self.User_FirstName} {self.User_LastName}({self.User_BookedOn})"


class Queries(models.Model):
    User_id = models.AutoField(primary_key=True)
    User_Name = models.CharField(max_length=50, default=' ')
    User_Email = models.EmailField(max_length=50)
    User_Contact = models.CharField(max_length=10, null=True)
    User_QueryDate = models.DateField(auto_now_add=True)
    User_Discription = models.TextField(max_length=500)
    def __str__(self):
        return f"{self.User_Name} ({self.User_QueryDate})"