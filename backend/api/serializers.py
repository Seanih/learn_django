# import default User class
from django.contrib.auth.models import User

# converts python to json and vice/versa with serializers
from rest_framework import serializers
from .models import Note


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password"]
        # prevent django from returning password info for users
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ["id", "title", "content", "created_at", "author"]
        # prevent user from setting who the author is
        extra_kwargs = {"author": {"read_only": True}}
