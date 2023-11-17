from django.db import models


class BaseProductModel(models.Model):
    price = models.FloatField()
    image = models.ImageField(upload_to="%Y/%m/%d")
    title = models.CharField(max_length=255)
    сreated = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        abstract = True


class Milk(BaseProductModel):
    pass


class Bread(BaseProductModel):
    pass


class FruitVegetables(BaseProductModel):
    pass


class FrozenProduct(BaseProductModel):
    pass


class Beverage(BaseProductModel):
    pass


class Confectionary(BaseProductModel):
    pass


class TeaCoffe(BaseProductModel):
    pass


class Balakleya(BaseProductModel):
    pass


class HealthyFood(BaseProductModel):
    pass


class PetProduct(BaseProductModel):
    pass


class BabyFood(BaseProductModel):
    pass


class Meat(BaseProductModel):
    pass


class NonFoodProduct(BaseProductModel):
    pass
