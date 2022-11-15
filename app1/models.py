

from datetime import datetime
from email.policy import default
from django.db import models
 
# Create your models here.

class items_data(models.Model):
 

    Name = models.CharField(max_length=30)
    Cost = models.IntegerField()
    timing=models.DateTimeField(blank=True,null=True)
    Description = models.CharField(max_length=30,null=True)
    Upload = models.ImageField(null=True,blank=True,upload_to="images/")
    Current_Time= models.DateTimeField(auto_now_add=True,blank=True)
    
    Top_Bidder = models.CharField(max_length=30,null=True,blank=True)
    def __str__(self):
        return self.Name

# class it(models.Model):
#     i_name = models.CharField(max_length=30)
#     timing=models.DateTimeField()
    
#     # Timing = models.DateTimeField()

#     def __str__(self):
#         return self.i_name
