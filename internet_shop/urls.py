from django.urls import path
from .views import *
from .detail_views import *

urlpatterns = [
    path(
        "product_info/bread/<int:pk>/",
        DetailProductsBread.as_view(),
        name="detail-products-bread",
    ),
    path(
        "product_info/fruits-and-vegetables/<int:pk>/",
        DetailProductsFruitsAndVegetables.as_view(),
        name="detail-products-fruits-and-vegetables",
    ),
    path(
        "product_info/frozen/<int:pk>/",
        DetailProductsFrozen.as_view(),
        name="detail-products-frozen",
    ),
    path(
        "product_info/beverages/<int:pk>/",
        DetailProductsBeverages.as_view(),
        name="detail-products-beverages",
    ),
    path(
        "product_info/confectionary/<int:pk>/",
        DetailProductsConfectionary.as_view(),
        name="detail-products-confectionary",
    ),
    path(
        "product_info/tea-and-coffee/<int:pk>/",
        DetailProductsTeaAndCoffee.as_view(),
        name="detail-products-tea-and-coffee",
    ),
    path(
        "product_info/balakleya/<int:pk>/",
        DetailProductsBalakleya.as_view(),
        name="detail-products-balakleya",
    ),
    path(
        "product_info/healthy-foods/<int:pk>/",
        DetailProductsHealthyFoods.as_view(),
        name="detail-products-healthy-foods",
    ),
    path(
        "product_info/pet/<int:pk>/",
        DetailProductsPet.as_view(),
        name="detail-products-pet",
    ),
    path(
        "product_info/baby-food/<int:pk>/",
        DetailProductsBabyFood.as_view(),
        name="detail-products-baby-food",
    ),
    path(
        "product_info/meat-poultry-sausage/<int:pk>/",
        DetailProductsMeatPoultrySausage.as_view(),
        name="detail-products-meat-poultry-sausage",
    ),
    path(
        "product_info/non-food/<int:pk>/",
        DetailProductsNonFood.as_view(),
        name="detail-products-non-food",
    ),
    path("product_info/milk-cheese-egg/<int:pk>/", DetailProductsMilks.as_view()),
    # --------------------------
    #---------------------------
    #---------------------------
    path("milks_list/", ListProductsMilks.as_view(), name="milks-list"),
    path("bread_list/", ListProductsBread.as_view(), name="bread-list"),
    path(
        "fruits_vegetables_list/",
        ListProductsFruitsAndVegetables.as_view(),
        name="fruits-vegetables-list",
    ),
    path(
        "frozen_products_list/",
        ListProductsFrozen.as_view(),
        name="frozen-products-list",
    ),
    path("beverages_list/", ListProductsBeverages.as_view(), name="beverages-list"),
    path(
        "confectionary_list/",
        ListProductsConfectionary.as_view(),
        name="confectionary-list",
    ),
    path(
        "tea_coffee_list/", ListProductsTeaAndCoffee.as_view(), name="tea-coffee-list"
    ),
    path("balakleya_list/", ListProductsBalakleya.as_view(), name="balakleya-list"),
    path(
        "healthy_foods_list/",
        ListProductsHealthyFoods.as_view(),
        name="healthy-foods-list",
    ),
    path("pet_products_list/", ListProductsPet.as_view(), name="pet-products-list"),
    path("baby_food_list/", ListProductsBabyFood.as_view(), name="baby-food-list"),
    path(
        "meat_poultry_sausage_list/",
        ListProductsMeatPoultrySausage.as_view(),
        name="meat-poultry-sausage-list",
    ),
    path(
        "non_food_products_list/",
        ListProductsNonFood.as_view(),
        name="non-food-products-list",
    ),
]
