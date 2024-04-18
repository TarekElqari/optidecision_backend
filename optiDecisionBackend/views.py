# views.py
from rest_framework import viewsets
from .models import Project, Criteria, SubCriteria
from .serializers import ProjectSerializer, CriteriaSerializer, SubCriteriaSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class CriteriaViewSet(viewsets.ModelViewSet):
    queryset = Criteria.objects.all()
    serializer_class = CriteriaSerializer


class SubCriteriaViewSet(viewsets.ModelViewSet):
    queryset = SubCriteria.objects.all()
    serializer_class = SubCriteriaSerializer
