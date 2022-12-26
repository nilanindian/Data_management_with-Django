import django_filters

from .models import myrecord

class myfilter(django_filters.FilterSet):
    class Meta:
        model=myrecord
        fields='__all__'
        #fields = ['id', 'name', 'city','phone' ] 
