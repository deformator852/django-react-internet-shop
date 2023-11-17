from rest_framework import generics
from .models import *
from .serializers import *

class DetailProductsMilks(generics.RetrieveAPIView):
    queryset = Milk.objects.all()
    serializer_class = ProductsMilk
    lookup_field = "pk"


class DetailProductsBread(generics.RetrieveAPIView):
    queryset = Bread.objects.all()
    serializer_class = ProductsBread


class DetailProductsFruitsAndVegetables(generics.RetrieveAPIView):
    queryset = FruitVegetables.objects.all()
    serializer_class = ProductsFruitsAndVegetables


class DetailProductsFrozen(generics.RetrieveAPIView):
    queryset = FrozenProduct.objects.all()
    serializer_class = ProductsFrozenProducts


class DetailProductsBeverages(generics.RetrieveAPIView):
    queryset = Beverage.objects.all()
    serializer_class = ProductsBeverages


class DetailProductsConfectionary(generics.RetrieveAPIView):
    queryset = Confectionary.objects.all()
    serializer_class = ProductsConfectionaryProducts


class DetailProductsTeaAndCoffee(generics.RetrieveAPIView):
    queryset = TeaCoffe.objects.all()
    serializer_class = ProductsTeaAndCoffee


class DetailProductsBalakleya(generics.RetrieveAPIView):
    queryset = Balakleya.objects.all()
    serializer_class = ProductsBalakleya


class DetailProductsHealthyFoods(generics.RetrieveAPIView):
    queryset = HealthyFood.objects.all()
    serializer_class = ProductsHealthyFoods


class DetailProductsPet(generics.RetrieveAPIView):
    queryset = PetProduct.objects.all()
    serializer_class = ProductsPetProducts


class DetailProductsBabyFood(generics.RetrieveAPIView):
    queryset = BabyFood.objects.all()
    serializer_class = ProductsBabyFood


class DetailProductsMeatPoultrySausage(generics.RetrieveAPIView):
    queryset = Meat.objects.all()
    serializer_class = ProductsMeatPoultrySausage


class DetailProductsNonFood(generics.RetrieveAPIView):
    queryset = NonFoodProduct.objects.all()
    serializer_class = NonFoodProduct
