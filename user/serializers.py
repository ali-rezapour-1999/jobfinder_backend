from rest_framework import serializers


class RegisterSerializer(serializers.Serializer):
    email = serializers.EmailField()


class VerifyEmailSerializer(serializers.Serializer):
    email = serializers.EmailField()
    code = serializers.CharField()


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()


class VerifyLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    code = serializers.CharField()
