from django_filters import rest_framework as filters
from ..models import Food


class CustomImageFieldFilter(filters.BaseCSVFilter, filters.CharFilter):
    pass

# Defining FilterSet for the Food model
class FoodFilter(filters.FilterSet):
    # Each field in the model can be used as a filter
    image = CustomImageFieldFilter(field_name='image', lookup_expr='exact')
    NO = filters.NumberFilter(field_name='NO')
    SAMPLE_ID = filters.NumberFilter(field_name='SAMPLE_ID')
    Food_Code = filters.NumberFilter(field_name='Food_Code')
    DB_Group = filters.CharFilter(field_name='DB_Group')
    Commercial_Product = filters.CharFilter(field_name='Commercial_Product')
    Food_Name = filters.CharFilter(field_name='Food_Name')
    Year = filters.NumberFilter(field_name='Year')
    Manufacturer_Distributor = filters.CharFilter(field_name='Manufacturer_Distributor')
    Food_Major_Category = filters.CharFilter(field_name='Food_Major_Category')
    Food_Subcategory = filters.CharFilter(field_name='Food_Subcategory')
    Single_Serving_Size = filters.NumberFilter(field_name='Single_Serving_Size')
    Content_Unit = filters.CharFilter(field_name='Content_Unit')
    Total_Content_g = filters.NumberFilter(field_name='Total_Content_g')
    Total_Content_mL = filters.NumberFilter(field_name='Total_Content_mL')
    Energy_kcal = filters.NumberFilter(field_name='Energy_kcal')
    Protein_g = filters.NumberFilter(field_name='Protein_g')
    Fat_g = filters.NumberFilter(field_name='Fat_g')
    Carbohydrates_g = filters.NumberFilter(field_name='Carbohydrates_g')
    Total_Sugars_g = filters.NumberFilter(field_name='Total_Sugars_g')


    class Meta:
        model = Food
        fields = '__all__'  # This allows filtering by every field in the model
        filter_overrides = {
            Food._meta.get_field('image'): {
                'filter_class': CustomImageFieldFilter,
            },
        }

# food_list = Food.objects.all()

# filterset = FoodFilter(data=request.GET, queryset=food_list)
# filtered_qs = filterset.qs