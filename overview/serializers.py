from rest_framework import serializers
from .models import Overview
import ipdb


class OverviewSerializer(serializers.ModelSerializer):
    bmi_classification = serializers.SerializerMethodField()

    whr_classification = serializers.SerializerMethodField()

    def get_bmi_classification(self, obj):
        if int(obj.bmi) < 18.5:
            return 'underweight'

        if int(obj.bmi) >= 18.5 and int(obj.bmi) < 25:
            return 'normal'

        if int(obj.bmi) >= 25 and int(obj.bmi) < 30:
            return 'overweight'

        if int(obj.bmi) >= 30 and int(obj.bmi) < 35:
            return 'obese'

        if int(obj.bmi) >= 35:
            return 'extremely obese'
          

    def get_whr_classification(self, obj):
        if obj.sex == 'female' and int(obj.whr) <= 0.80:
            return 'low'

        if obj.sex == 'female' and int(obj.whr) > 0.80 and int(obj.whr) <= 0.85:
            return 'moderate'

        if obj.sex == 'female' and int(obj.whr) > 0.85:
            return 'high'
        
        if obj.sex == 'male' and int(obj.whr) <= 0.95:
            return 'low'

        if obj.sex == 'male' and int(obj.whr) > 0.95 and int(obj.whr) < 1.0:
            return 'moderate'

        if obj.sex == 'male' and int(obj.whr) >= 1.0:
            return 'high'

        

    class Meta:
        model = Overview

        fields = [
            'id',
            'sex',
            'height',
            'weight',
            'bmi',
            'bmi_classification',
            'whr',
            'whr_classification',
            'lean_mass',
            'fat_mass',
            'body_fat',
            'created_at',
            'created_by'
        ]

        read_only_fields = [
            'bmi_classification',
            'whr_classification',
            'created_at',
            'created_by'
        ]


    def create(self, validated_data: dict) -> Overview:
        return Overview.objects.create(**validated_data)
