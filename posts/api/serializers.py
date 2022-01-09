from rest_framework import serializers
from posts.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'id',
            'user',
            'content',
            'image'
        ]
        read_only_fields = ['user']

    def validate(self, data):
        content = data.get("content", None)
        if content == "":
            content = None
        image = data.get("image", None)
        if content is None and image is None:
            raise serializers.ValidationError("Content and Image are required")
        return data
