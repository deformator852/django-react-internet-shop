from rest_framework import generics
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.views import APIView

class ListProductsMilks(APIView):
    def get(self, request, *args, **kwargs):
        milks = Milk.objects.all()
        serialized_milks = ProductsMilk(milks, many=True, context={'request': request}).data

        grouped_milks = [serialized_milks[i:i+3] for i in range(0, len(serialized_milks), 3)]

        return Response(grouped_milks)


class ListProductsBread(generics.ListAPIView):
    queryset = Bread.objects.all()
    serializer_class = ProductsBread


class ListProductsFruitsAndVegetables(generics.ListAPIView):
    queryset = FruitVegetables.objects.all()
    serializer_class = ProductsFruitsAndVegetables


class ListProductsFrozen(generics.ListAPIView):
    queryset = FrozenProduct.objects.all()
    serializer_class = ProductsFrozenProducts


class ListProductsBeverages(generics.ListAPIView):
    queryset = Beverage.objects.all()
    serializer_class = ProductsBeverages


class ListProductsConfectionary(generics.ListAPIView):
    queryset = Confectionary.objects.all()
    serializer_class = ProductsConfectionaryProducts


class ListProductsTeaAndCoffee(generics.ListAPIView):
    queryset = TeaCoffe.objects.all()
    serializer_class = ProductsTeaAndCoffee


class ListProductsBalakleya(generics.ListAPIView):
    queryset = Balakleya.objects.all()
    serializer_class = ProductsBalakleya


class ListProductsHealthyFoods(generics.ListAPIView):
    queryset = HealthyFood.objects.all()
    serializer_class = ProductsHealthyFoods


class ListProductsPet(generics.ListAPIView):
    queryset = PetProduct.objects.all()
    serializer_class = ProductsPetProducts


class ListProductsBabyFood(generics.ListAPIView):
    queryset = BabyFood.objects.all()
    serializer_class = ProductsBabyFood


class ListProductsMeatPoultrySausage(generics.ListAPIView):
    queryset = Meat.objects.all()
    serializer_class = ProductsMeatPoultrySausage


class ListProductsNonFood(generics.ListAPIView):
    queryset = NonFoodProduct.objects.all()
    serializer_class = NonFoodProduct
