from django.db import models

# Create your models here.
class Echo(models.Model):
    echoMessage = models.CharField(max_length=60)


    def __str__(self):
        return self.echoMessage