from rest_framework import serializers

from store.models import Contact, Product, Retail


class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = "__all__"


class RetailSerializer(serializers.ModelSerializer):
    products = ProductSerializer(read_only=True, many=True)
    contacts = ContactSerializer(read_only=True)

    class Meta:
        model = Retail
        fields = "__all__"
