from django.contrib.auth import authenticate
from rest_framework import serializers


from .models import User


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        extra_kwargs = {"password": {"write_only": True}}

        def create(self,validated_data):
            return User.objects.create_user(**validated_data)


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=100)

    def create(self, validated_data):
        # print(validated_data,"hello")
        user=authenticate(**validated_data)
        self.context.update({'user':user})
        return user
