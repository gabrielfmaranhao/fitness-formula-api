from rest_framework import serializers
from .models import Rating

class RatingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rating
        fields = ["id", "comment", "stars", "student", "trainer",]

        read_only_fields = ["student", "trainer",]