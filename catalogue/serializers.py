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
            'functions',
            'themes',
            'comments',
            'added_date',
            'updated_date'
        )


class ThemeSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='theme_detail', format='json')

    class Meta:
        model = models.Theme
        fields = (
            'id',
            'url',
            'name',
            'parent_theme',
            'level',
            'comments',
            'added_date',
            'updated_date'
        )


class TypeRessourceSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='type_ressource_detail', format='json')

    class Meta:
        model = models.TypeRessource
        fields = (
            'id',
            'url',
            'name',
            'comments',
            'function',
            'added_date',
            'updated_date'
        )


class RessourceSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='ressource_detail', format='json')

    class Meta:
        model = models.Ressource
        fields = (
            'id',
            'url',
            'name',
            'url',
            'themes',
            'type_ressource',
            'comments',
            'function',
            'added_date',
            'updated_date'
        )
