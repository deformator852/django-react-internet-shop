from django.urls import path
from .views import * 

urlpatterns = [
    path("milks_list/", ListProductsMilks.as_view(), name="milks-list"),
    path("bread_list/", ListProductsBread.as_view(), name="bread-list"),
    path("fruits_vegetables_list/", ListProductsFruitsAndVegetables.as_view(), name="fruits-vegetables-list"),
    path("frozen_products_list/", ListProductsFrozen.as_view(), name="frozen-products-list"),
    path("beverages_list/", ListProductsBeverages.as_view(), name="beverages-list"),
    path("confectionary_list/", ListProductsConfectionary.as_view(), name="confectionary-list"),
    path("tea_coffee_list/", ListProductsTeaAndCoffee.as_view(), name="tea-coffee-list"),
    path("balakleya_list/", ListProductsBalakleya.as_view(), name="balakleya-list"),
    path("healthy_foods_list/", ListProductsHealthyFoods.as_view(), name="healthy-foods-list"),
    path("pet_products_list/", ListProductsPet.as_view(), name="pet-products-list"),
    path("baby_food_list/", ListProductsBabyFood.as_view(), name="baby-food-list"),
    path("meat_poultry_sausage_list/", ListProductsMeatPoultrySausage.as_view(), name="meat-poultry-sausage-list"),
    path("non_food_products_list/", ListProductsNonFood.as_view(), name="non-food-products-list"),
]

