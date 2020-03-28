from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone



class Assembly(models.Model):
    manage = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    assembly = models.CharField(max_length=12)   
    mvl_No = models.CharField(max_length=12,blank=True) 
    qty = models.PositiveIntegerField()  
    fab_date = models.DateField(help_text="Fab arriving date, Please use the following format: <em>MM/DD/YY</em>.")   
    comments = models.TextField(blank=True)
    date_posted = models.DateTimeField(default=timezone.now)
    requestor = models.CharField(max_length=100,blank=True)  
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
    packing_no = models.CharField(max_length=120)       
    packing_file = models.FileField(upload_to='Packing', blank=True)
    comment = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    active = models.BooleanField(default=False)
    
    def __str__(self):
        return self.packing_no


class ShortageReport(models.Model):    
    manage = models.ForeignKey(User, on_delete=models.CASCADE,default=None)             
    assembly = models.CharField(max_length=50)      
    shortage_file = models.FileField(upload_to='Shortage', blank=True) 
    comment = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    active = models.BooleanField(default=False)
    
    def __str__(self):
        return self.assembly



class Quote(models.Model):
    manage = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    assembly = models.CharField(max_length=50)      
    quote_file = models.FileField(upload_to='Quote', blank=True)
    comment = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    active = models.BooleanField(default=False)		


    def __str__(self):
        return self.assembly

    


 