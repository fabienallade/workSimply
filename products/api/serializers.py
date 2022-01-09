from rest_framework import serializers

from products.models import Product


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = [
            'id',
            'title',
            'price',
            'description',
            'images',
            'category'
        ]

    def validate(self, data):
        title = data.get("title", None)
        if title == "":
            title = None
        image = data.get("image", None)
        if title is None and image\
                is None:
            raise serializers.ValidationError("title and Image are required")
        return data
