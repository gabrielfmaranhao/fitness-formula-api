from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User
import ipdb


class UserSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    username = serializers.CharField(
        max_length=20,
        validators=[
            UniqueValidator(
                queryset=User.objects.all(), message="username already taken."
            )
        ],
    )
    email = serializers.EmailField(
        max_length=127,
        validators=[
            UniqueValidator(
                queryset=User.objects.all(), message="email already registered."
            )
        ],
    )
    password = serializers.CharField(write_only=True)
    first_name = serializers.CharField(max_length=150)
    middle_name = serializers.CharField(max_length=150)
    last_name = serializers.CharField(max_length=150)
    cpf = serializers.CharField(max_length=11, min_length=11)
    birthdate = serializers.DateField()
    is_staff = serializers.BooleanField()
    is_superuser = serializers.BooleanField(read_only=True)

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            if key == "password":
                instance.set_password(value)
            else:
                setattr(instance, key, value)

        instance.save()

        return instance


class TrainerSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    username = serializers.CharField(
        max_length=20,
        validators=[
            UniqueValidator(
                queryset=User.objects.all(), message="username already taken."
            )
        ],
    )
    email = serializers.EmailField(
        max_length=127,
        validators=[
            UniqueValidator(
                queryset=User.objects.all(), message="email already registered."
            )
        ],
    )
    password = serializers.CharField(write_only=True)
    first_name = serializers.CharField(max_length=150)
    middle_name = serializers.CharField(max_length=150)
    last_name = serializers.CharField(max_length=150)
    cpf = serializers.CharField(max_length=11, min_length=11)
    birthdate = serializers.DateField()
    is_staff = serializers.BooleanField()
    is_superuser = serializers.BooleanField(read_only=True)
    rating = serializers.SerializerMethodField()

    def get_rating(self, obj):
        ...
