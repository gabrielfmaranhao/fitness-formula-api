from datetime import datetime
from rest_framework import serializers
from .models import Sheet


class SheetSerializer(serializers.ModelSerializer):
    # duration = serializers.SerializerMethodField()

    # def get_duration(self, obj: Sheet):
    #     start_date = datetime.strptime(obj.created_at, "%Y/%m/%d")
    #     end_date = datetime.strptime(obj.until, "%Y/%m/%d")
    #     delta = end_date - start_date

    #     return f"{delta.days} days"

    class Meta:
        model = Sheet
        fields = [
            "id",
            "type",
            "created_at",
            "until",
            # "duration",
            "trainer",
            "student",
        ]
        read_only_fields = [
            "trainer",
            "student",
        ]
