from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from optiDecisionBackend import views

router = routers.DefaultRouter()
# Remove the registration of SubCriteriaViewSet
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
