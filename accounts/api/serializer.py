from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class AccountRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
        ]
        extract_kwargs = {'password': {'write_only': True}}
