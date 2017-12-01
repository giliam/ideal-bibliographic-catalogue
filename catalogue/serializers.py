#coding:utf-8

from rest_framework import serializers
from rest_framework import pagination
from catalogue import models


class FunctionSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='function_detail', format='json')

    class Meta:
        model = models.Function
        fields = (
            'id', 
            'url', 
            'name', 
            'comments', 
            'added_date', 
            'updated_date'
        )


class PersonSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='person_detail', format='json')

    class Meta:
        model = models.Person
        fields = (
            'id', 
            'url', 
            'firstname', 
            'lastname', 
            'comments', 
            'function', 
            'added_date', 
            'updated_date'
        )
