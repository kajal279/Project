

from django.contrib import admin
from testapp.models import Ride_Book
# Register your models here.
class Ride_Admin(admin.ModelAdmin):
    list_display = [ 'ride_Id' ,'ride_source','ride_designation']

admin.site.register(Ride_Book,Ride_Admin)