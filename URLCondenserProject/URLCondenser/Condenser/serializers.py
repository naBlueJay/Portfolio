from rest_framework import serializers
from . models import URLData

# takes the data and serializes it. Pretty straight forward
# should convert the data into a jason type file
class URLDataSerializers(serializers.ModelSerializer):
    class Meta:
        model = URLData
        field = '__all__'