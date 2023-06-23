
from rest_framework import serializers
from person_app.models import Person

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['first_name','last_name','age','email_id','phone_number','date_of_birth','username','password']

        