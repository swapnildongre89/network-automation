from django.db import models

# Create your models here.

class Devices(models.Model):
    hostname= models.CharField(max_length=50, blank=False)
    ipadd= models.GenericIPAddressField(default="0.0.0.0")

    choices = (
        ('JC', 'Johns Creek'),
        ('LW', 'Lewisville'),
        ('PHX', 'Phoenix'),
    )
    
    datacenter= models.CharField(max_length=30, choices=choices, default='LW')

    class Meta:
        abstract= True

    def __str__(self):
        return (f"Hostname: {self.hostname}, IP_Address: {self.ipadd}, Datacenter: {self.datacenter}")

class Routers(Devices):
    pass

class Switches(Devices):
    pass

class Firewalls(Devices):
    pass

class Loadbalancers(Devices):
    pass
