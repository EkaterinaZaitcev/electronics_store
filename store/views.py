from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from store.models import Retail, Contact, Product
from store.permissions import IsActive
from store.serializers import RetailSerializer, ContactSerializer, ProductSerializer


class RetailViewSet(viewsets.ModelViewSet):
    queryset = Retail.objects.all()
    serializer_class = RetailSerializer
    permission_classes = (IsActive,)
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ("contacts_country",)


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = (IsActive,)
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ("country",)


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsActive,)
