from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# from django.urls import reverse


class Assembly(models.Model):
    manage = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    assembly = models.CharField(max_length=12, unique=True)   
    mvl_No = models.CharField(max_length=12, unique=True, blank=True) 
    qty = models.PositiveIntegerField(unique=True)  
    fab_date = models.CharField(max_length=10, unique=True)   
    comments = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    requestor = models.CharField(max_length=100, unique=False,blank=True)  
    image = models.ImageField(default='default1.png', upload_to='boards', blank=True)
    image1 = models.ImageField(default='default1.png', upload_to='boards', blank=True)
    image2 = models.ImageField(default='default1.png', upload_to='boards', blank=True)
    image3 = models.ImageField(default='default1.png', upload_to='boards', blank=True)   
    delivery = models.CharField(max_length=20, blank=True)
    status = models.TextField(blank=True)    
    done = models.BooleanField(default=False)

    class Meta:
        verbose_name='assembly'
        verbose_name_plural = 'assemblies'
        db_table = 'Assembly'
        ordering = ['-date_posted'] 		
		

    
    def __str__(self):
        return self.assembly 



class Packing(models.Model):
    manage = models.ForeignKey(User, on_delete=models.CASCADE,default=None)    
    packing_no = models.CharField(max_length=120, unique=False)       
    packing_file = models.FileField(upload_to='Packing', blank=True)
    comment = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    active = models.BooleanField(default=False)
    
    def __str__(self):
        return self.packing_no


class ShortageReport(models.Model):    
    manage = models.ForeignKey(User, on_delete=models.CASCADE,default=None)             
    assembly = models.CharField(max_length=50, unique=False)      
    shortage_file = models.FileField(upload_to='Shortage', blank=True) 
    comment = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    active = models.BooleanField(default=False)
    
    def __str__(self):
        return self.assembly



class Quote(models.Model):
    manage = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    assembly = models.CharField(max_length=50, unique=False)      
    quote_file = models.FileField(upload_to='Quote', blank=True)
    comment = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    active = models.BooleanField(default=False)		


    def __str__(self):
        return self.assembly

    


 