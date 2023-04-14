from .serializer import FoodSerializer
from items.models import Food
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin
from django_filters.rest_framework import DjangoFilterBackend
from .filters import FoodFilter


class FoodViewSet(ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = FoodFilter
    search_fields = ['Food_Name', 'Commercial_Product', 'Manufacturer_Distributor', 'Food_Major_Category', 'Food_Subcategory']
    ordering_fields = ['Energy_kcal', 'Protein_g', 'Fat_g', 'Carbohydrates_g', 'Total_Sugars_g']
    pagenation_class = PageNumberPagination


