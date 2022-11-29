from django.db import models
from datetime import datetime, timedelta
# Create your models here.

class Person(models.Model) :
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField(default=0)
    gender = models.CharField(max_length=10, blank=True)
    weight = models.DecimalField(max_digits=8, decimal_places=2)
    height_feet = models.IntegerField(default=0)
    height_inches = models.IntegerField(default=0)
    password = models.CharField(max_length=20)
    user_name = models.CharField(max_length=20)

    def __str__ (self) :
        return (self.full_name)

    @property
    def full_name(self) :
        return '%s %s' % (self.first_name, self.last_name)

class JournalEntry(models.Model) :
    date = models.DateField(default=datetime.today, blank=True)
    meal = models.CharField(max_length=20)
    food_name = models.CharField(max_length=50)
    servings = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__ (self) :
        return (self.food_name)

class dailyNutritionalTotals(models.Model) :
    date = models.DateField(default=datetime.today, blank=True)
    serum_k_total = models.DecimalField(max_digits=8, decimal_places=2)
    serum_phos_total = models.DecimalField(max_digits=8, decimal_places=2)
    serum_na_total = models.DecimalField(max_digits=8, decimal_places=2)
    serum_creatine_total = models.DecimalField(max_digits=8, decimal_places=2)
    serum_albumin_total = models.DecimalField(max_digits=8, decimal_places=2)
    serum_blood_sugar_total = models.DecimalField(max_digits=8, decimal_places=2)
    DV_sodium_total = models.DecimalField(max_digits=8, decimal_places=2)
    DV_protein_total = models.DecimalField(max_digits=8, decimal_places=2)
    DV_water_total = models.DecimalField(max_digits=8, decimal_places=2)
    DV_k_total = models.DecimalField(max_digits=8, decimal_places=2)
    DV_phos_total = models.DecimalField(max_digits=8, decimal_places=2)

    #what value to show as self name?
    #def __str__ (self) :
     #   return (self.food_name)