from .models import todotask
from rest_framework import serializers


class taskserializer(serializers.ModelSerializer):
    class Meta:
        model=todotask
        fields=['slno','title','description','due_date']
        