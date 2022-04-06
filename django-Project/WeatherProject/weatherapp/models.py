from django.db import models
from django.contrib.gis.db import models
# Create your models here.
class Point(models.Model):
    address=models.CharField(max_length=20,blank=True,null=True)
    Location=models.PointField(srid=4326,blank=True,null=True)
    humidity=models.IntegerField()
    Temperature=models.IntegerField()
    def __str__(self):
        return self.address