from django.db import models

# Create your models here.
class Branches(models.Model):
    district=models.CharField(max_length=250)
    details=models.TextField()

    def __str__(self):
        return self.district


class subbranches(models.Model):
    district=models.ForeignKey(Branches,on_delete=models.CASCADE)
    subbranches=models.CharField(max_length=250)

    def __str__(self):
        return self.subbranches



