from django.db import models
from django.contrib.auth.models import User



class Ride_Book(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ride_Id=models.IntegerField(null=True, blank=True)
    ride_source=models.CharField(max_length=20, null=False, blank=False)
    ride_designation = models.CharField(max_length=20, null=False, blank=False)
    ride_distance = models.IntegerField(null=True, blank=True)
    ride_status = models.BooleanField()

    class Meta:
        ordering = ('ride_Id',)

    def __str__(self):
        return "{0} - {1}".format(self.user.username, self.ride_Id)