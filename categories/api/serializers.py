from rest_framework import serializers

from categories.models import Category


class CategorySerializer(serializers.ModelSerializer):
    icon = serializers.SerializerMethodField

    class Meta:
        model = Category
        fields = [
            'id',
            'name',
            'icon',
            'color',
            'image'
        ]

    def get_icon(self, obj):
        return obj.get_icon_display()

    def validate(self, data):
        content = data.get("name", None)
        if content == "":
            content = None
        if content is None:
            raise serializers.ValidationError("Name is required")
        return data
