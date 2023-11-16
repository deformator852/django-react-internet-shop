from django.db import models


class Milk(models.Model):
    price = models.FloatField()
    image = models.ImageField(upload_to="%Y/%m/%d")
    title = models.CharField(max_length=255)
    сreated = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.title


class Bread(models.Model):
    price = models.FloatField()
    image = models.ImageField(upload_to="%Y/%m/%d")
    title = models.CharField(max_length=255)
    сreated = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)


class FruitVegetables(models.Model):
    price = models.FloatField()
    image = models.ImageField(upload_to="%Y/%m/%d")
    title = models.CharField(max_length=255)
    сreated = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)


class FrozenProduct(models.Model):
    price = models.FloatField()
    image = models.ImageField(upload_to="%Y/%m/%d")
    title = models.CharField(max_length=255)
    сreated = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)


class Beverage(models.Model):
    price = models.FloatField()
    image = models.ImageField(upload_to="%Y/%m/%d")
    title = models.CharField(max_length=255)
    сreated = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)


class Confectionary(models.Model):
    price = models.FloatField()
    image = models.ImageField(upload_to="%Y/%m/%d")
    title = models.CharField(max_length=255)
    сreated = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)


class TeaCoffe(models.Model):
    price = models.FloatField()
    image = models.ImageField(upload_to="%Y/%m/%d")
    title = models.CharField(max_length=255)
    сreated = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)


class Balakleya(models.Model):
    price = models.FloatField()
    image = models.ImageField(upload_to="%Y/%m/%d")
    title = models.CharField(max_length=255)
    сreated = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)


class HealthyFood(models.Model):
    price = models.FloatField()
    image = models.ImageField(upload_to="%Y/%m/%d")
    title = models.CharField(max_length=255)
    сreated = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)


class PetProduct(models.Model):
    price = models.FloatField()
    image = models.ImageField(upload_to="%Y/%m/%d")
    title = models.CharField(max_length=255)
    сreated = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)


class BabyFood(models.Model):
    price = models.FloatField()
    image = models.ImageField(upload_to="%Y/%m/%d")
    title = models.CharField(max_length=255)
    сreated = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)


class Meat(models.Model):
    price = models.FloatField()
    image = models.ImageField(upload_to="%Y%m%d")
    title = models.CharField(max_length=255)
    сreated = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)


class NonFoodProduct(models.Model):
    price = models.FloatField()
    image = models.ImageField(upload_to="%Y/%m/%d")
    title = models.CharField(max_length=255)
    сreated = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
