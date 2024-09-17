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
    classification = models.CharField(unique=True, max_length=100)
    name = models.CharField(max_length=200)
    department = models.CharField(choices=DEPARTMENT, default="CHOOSE DEPARTMENT", max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    basic_holder = models.CharField(default="Central Registry", max_length=50)
    dispatched_at = models.DateTimeField(blank=False)
    
    def __str__ (self):
        return self.classification + "..." + self.name
    

class Filemovement(models.Model):
    movement = models.ForeignKey(Filelog, on_delete=models.CASCADE)
    current_holder = models.CharField(max_length=200, blank=False)
    date_received = models.DateTimeField(auto_now_add=True, blank=False)

    
        



