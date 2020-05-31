from django.db import models  

class grzyb(models.Model):  
    name = models.CharField(max_length=100)  
    latin = models.CharField(max_length=100) 
    edible = models.CharField(max_length=15)  
    occurence = models.CharField(max_length=100) 
    class Meta:  
        db_table = "grzyb"  