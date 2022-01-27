from .models import Customer
from rest_framework import serializers


class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'username', 'gender', 'is_customer']
        extra_kwargs = {"username": {"error_messages": {"required": "Username can not be blank"}}}