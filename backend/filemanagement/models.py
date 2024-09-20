from django.db import models

# Create your models here.
DEPARTMENT = [
        ('CHOOSE DEPARTMENT','Choose Department'),
        ('ADM','Administration'),
        ('HR','Human Resources'),
        ('PUB','Publicity & Communications'),
        ('PROC','Procurement'),
        ('PRM','Property Management'),
        ('CBN','Claims & Benefits'),
        ('HSP','Hospitals'),
        ('MEM','Membership'),
        ('LEG','Legal'),
        ('TRS','Transport'),
        ('REP','Reports'),
        ('ST','Standards'),
        ('FIN','Finance'),
        ('C','Confidential')
    ]


class Filelog(models.Model):
    classification = models.CharField(unique=True, max_length=100, blank=False)
    #unique=true will prevent duplication
    name_of_file = models.CharField(max_length=200, blank=False)
    department = models.CharField(choices=DEPARTMENT, default="CHOOSE DEPARTMENT", max_length=50)
    created_at = models.DateField(auto_now_add=True, blank=False)
    basic_holder = models.CharField(default="Central Registry", max_length=50)
    dispatched_at = models.DateField(blank=False)
    closed = models.BooleanField(blank=False)
    
    
    def __str__ (self):
        return self.classification + "   " + self.name_of_file
    

class Filemovement(models.Model):
    file = models.ForeignKey(Filelog, on_delete=models.CASCADE)
    #related name allows me to see all the movements related to one file
    name_of_holder = models.CharField(max_length=200, blank=False)
    location_of_holder = models.CharField(max_length=100, blank=False)
    date_received = models.DateTimeField(auto_now_add=True, blank=False)

    def __str__(self):
        return self.file.name_of_file + "   moved to   " + self.location_of_holder + "   by   " + self.name_of_holder


    
        



