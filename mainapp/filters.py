import django_filters
from mainapp.models import *

class CollectionFilter(django_filters.FilterSet):
    
    class Meta:
        model = Collection
        fields = '__all__'
        exclude = ['customer', 'description']

class CustomerFilter(django_filters.FilterSet):

    class Meta:
        model = Customer
        fields = '__all__'
        exclude = ['due', 'address', 'date_added', 'user']