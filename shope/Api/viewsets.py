from rest_framework.viewsets import ModelViewSet
from shope.Api.serializers import CategorySerializer
from shope.models import Product
class CategoryViewSet(ModelViewSet):
    queryset = Product.objects.filter(parent=None)
    serializer_class = CategorySerializer

    def get_queryset(self):
        parent = self.request.query_params.get("parent")
        queryset = Product.objects.filter(parent=parent).select_related("parent") if parent else self.queryset
        return queryset