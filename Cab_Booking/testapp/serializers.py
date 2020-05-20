from rest_framework.serializers import ModelSerializer
from testapp.models import Ride_Book
class Ride_BookSerializer(ModelSerializer):
    class Meta:
        model=Ride_Book
        fields="__all__"