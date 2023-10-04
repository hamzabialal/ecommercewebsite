from django.urls import include, path
from rest_framework.routers import DefaultRouter

from shope.Api.viewsets import CategoryViewSet

router = DefaultRouter()


router.register("category", CategoryViewSet, basename="categories")


urlpatterns = [
    path("", include(router.urls)),
]