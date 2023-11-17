from rest_framework import generics
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.views import APIView


class BaseListView(APIView):
    model = None
    serializer_class = None

    def get(self, request, *args, **kwargs):
        products = self.model.objects.all()
        serialized_products = self.serializer_class(
            products, many=True, context={"request": request}
        ).data
        grouped_products = [
            serialized_products[i : i + 3]
            for i in range(0, len(serialized_products), 3)
        ]

        return Response(grouped_products)

class ListProductsMilks(BaseListView):
    model = Milk
    serializer_class = ProductsMilk


class ListProductsBread(BaseListView):
    queryset = Bread
    serializer_class = ProductsBread


class ListProductsFruitsAndVegetables(BaseListView):
    queryset = FruitVegetables
    serializer_class = ProductsFruitsAndVegetables


class ListProductsFrozen(BaseListView):
    queryset = FrozenProduct
    serializer_class = ProductsFrozenProducts


class ListProductsBeverages(BaseListView):
    queryset = Beverage
    serializer_class = ProductsBeverages


class ListProductsConfectionary(BaseListView):
    queryset = Confectionary
    serializer_class = ProductsConfectionaryProducts


class ListProductsTeaAndCoffee(BaseListView):
    queryset = TeaCoffe
    serializer_class = ProductsTeaAndCoffee


class ListProductsBalakleya(BaseListView):
    queryset = Balakleya
    serializer_class = ProductsBalakleya


class ListProductsHealthyFoods(BaseListView):
    queryset = HealthyFood
    serializer_class = ProductsHealthyFoods


class ListProductsPet(BaseListView):
    queryset = PetProduct
    serializer_class = ProductsPetProducts


class ListProductsBabyFood(BaseListView):
    queryset = BabyFood
    serializer_class = ProductsBabyFood


class ListProductsMeatPoultrySausage(BaseListView):
    queryset = Meat
    serializer_class = ProductsMeatPoultrySausage


class ListProductsNonFood(BaseListView):
    queryset = NonFoodProduct
    serializer_class = NonFoodProduct
