# serializers.py
from rest_framework import serializers
from .models import Project, Criteria, SubCriteria


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class CriteriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Criteria
        fields = '__all__'


class SubCriteriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCriteria
        fields = '__all__'
