from rest_framework import serializers
from .models import *


class BaseProductSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        abstract = True

    def get_image(self, obj):
        request = self.context.get("request")
        if obj.image:
            return request.build_absolute_uri(obj.image.url)
        return None


class ProductsMilk(BaseProductSerializer):
    class Meta:
        model = Milk
        fields = ["price", "image", "title","id"]



class ProductsBread(BaseProductSerializer):
    class Meta:
        model = Bread
        fields = ["price", "image", "title","id"]


class ProductsFruitsAndVegetables(BaseProductSerializer):
    class Meta:
        model = FruitVegetables
        fields = ["price", "image", "title","id"]


class ProductsFrozenProducts(BaseProductSerializer):
    class Meta:
        model = FrozenProduct
        fields = ["price", "image", "title","id"]


class ProductsBeverages(BaseProductSerializer):
    class Meta:
        model = Beverage
        fields = ["price", "image", "title","id"]


class ProductsConfectionaryProducts(BaseProductSerializer):
    class Meta:
        model = Confectionary
        fields = ["price", "image", "title","id"]


class ProductsTeaAndCoffee(BaseProductSerializer):
    class Meta:
        model = TeaCoffe
        fields = ["price", "image", "title","id"]


class ProductsBalakleya(BaseProductSerializer):
    class Meta:
        model = Balakleya
        fields = ["price", "image", "title","id"]


class ProductsHealthyFoods(BaseProductSerializer):
    class Meta:
        model = HealthyFood
        fields = ["price", "image", "title","id"]


class ProductsPetProducts(BaseProductSerializer):
    class Meta:
        model = PetProduct
        fields = ["price", "image", "title","id"]


class ProductsBabyFood(BaseProductSerializer):
    class Meta:
        model = BabyFood
        fields = ["price", "image", "title","id"]


class ProductsMeatPoultrySausage(BaseProductSerializer):
    class Meta:
        model = Meat
        fields = ["price", "image", "title","id"]


class NonFood(BaseProductSerializer):
    class Meta:
        model = NonFoodProduct
        fields = ["price", "image", "title","id"]
