import django_filters 

from .models import *

class PersonFilter(django_filters.FilterSet):
    class Meta:
        model = Person
        fields = {
                    'first_name':['icontains'],
                    'last_name':['icontains'],
                    'age':['exact'],
                }