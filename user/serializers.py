from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User
from rating.models import Rating
from django.db.models import Avg


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = [
            "groups",
            "user_permissions",
            "is_active",
            "last_login",
            "is_superuser",
        ]
        read_only_fields = ["id", "is_superuser"]
        extra_kwargs = {"password": {"write_only": True}}

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


class TrainerSerializer(serializers.ModelSerializer):
    rating = serializers.SerializerMethodField()

    def get_rating(self, obj):
        rating = Rating.objects.filter(trainer=obj).aggregate(avg_rating=Avg("stars"))[
            "avg_rating"
        ]

        return round(rating, 1)

    class Meta:
        model = User
        exclude = [
            "groups",
            "user_permissions",
            "is_active",
            "last_login",
            "is_superuser",
        ]
        read_only_fields = ["id", "is_superuser"]
        extra_kwargs = {"password": {"write_only": True}}
