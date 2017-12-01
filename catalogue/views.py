#coding:utf-8

from rest_framework import generics
from rest_framework import permissions
from rest_framework import response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.reverse import reverse

from catalogue import models
from catalogue import serializers


class FunctionList(generics.ListCreateAPIView):
    queryset = models.Function.objects.all()
    serializer_class = serializers.FunctionSerializer


class FunctionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Function.objects.all()
    serializer_class = serializers.FunctionSerializer


class PersonList(generics.ListCreateAPIView):
    queryset = models.Person.objects.all()
    serializer_class = serializers.PersonSerializer


class PersonDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Person.objects.all()
    serializer_class = serializers.PersonSerializer


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def api_root(request, format=None):
    return response.Response({
        'function_list': reverse('function_list', request=request, format=format),
        'person_list': reverse('person_list', request=request, format=format),
    })