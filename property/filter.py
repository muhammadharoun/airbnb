import django_filters
from .models import Property
class ProertyFilter(django_filters.FilterSet):
    class Meta:
        model = Property
        fields = ['name', 'description','place','category']

