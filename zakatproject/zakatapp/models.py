from django.db import models
from django.contrib.auth.models import User

class ZakatType(models.Model):
    ZAKAT_TYPES = [
        ('gold', 'Gold'),
        ('money', 'Money'),
        ('plant', 'plant'),
        ('silver', 'Silver'),
        ('livestock','Livestock'),
        
    ]
    zakat_typee = models.CharField(max_length=20, choices=ZAKAT_TYPES)
    def __str__(self):
        return self.zakat_typee
    
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username
    
class MoneyZakat(models.Model):
    YEAR_CHOICES = [
        ('M', 'ميلادي'),
        ('H', 'هجري'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=20, decimal_places=3)
    zakat_type = models.ForeignKey(ZakatType, on_delete=models.CASCADE)
    year_type = models.CharField(max_length=1, choices=YEAR_CHOICES)
    silver_price = models.DecimalField(max_digits=20, decimal_places=3)
    money=models.DecimalField(max_digits=20, decimal_places=3)

    def __str__(self):
        return f"{self.user.username}  {self.amount}"
    
class GoldZakat(models.Model):
    GOLD_KARAT = [
        ('10', '10'),
        ('14', '14'),
        ('18', '18'),
        ('21', '21'),
        ('22', '22'),
        ('24', '24'),
    ]
    
    YEAR_CHOICES = [
        ('M', 'ميلادي'),
        ('H', 'هجري'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    weight = models.DecimalField(max_digits=20, decimal_places=3)
    zakat_type = models.ForeignKey(ZakatType, on_delete=models.CASCADE)
    gold_karat = models.CharField(max_length=4, choices=GOLD_KARAT)
    amount = models.DecimalField(max_digits=20, decimal_places=3)
    year_type = models.CharField(max_length=1, choices=YEAR_CHOICES)
    Price_of_gram_of_gold =models.DecimalField(max_digits=20, decimal_places=3)

    def __str__(self):
        return f" {self.user.username}  {self.weight}"
    
class LivestockZakat(models.Model):
    ANIMAL_TYPES = [
        ('C', 'بقرة'),
        ('S', 'شاة'),
        ('G', 'ابل'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    animal_type = models.CharField(max_length=1, choices=ANIMAL_TYPES)
    count = models.IntegerField(default=0)
    amount=models.IntegerField(default=0)
    
    def __str__(self):
        return f" {self.user.username} {self.animal_type} {self.amount}" 
    
class SilverZakat(models.Model):
    YEAR_CHOICES = [
        ('M', 'ميلادي'),
        ('H', 'هجري'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    weight = models.DecimalField(max_digits=20, decimal_places=3)
    zakat_type = models.ForeignKey(ZakatType, on_delete=models.CASCADE)
    Price_of_gram_of_silver=models.DecimalField(max_digits=20, decimal_places=3)
    amount = models.DecimalField(max_digits=20, decimal_places=3)
    year_type = models.CharField(max_length=1, choices=YEAR_CHOICES)
    
    def __str__(self):
        return f"{self.user.username}  {self.weight}"
    
class PlantZakat(models.Model):
    IRRIGATION_METHOD = [
        ('Watering_at_a_cost', 'تسقى بتكلفه'),
        ('Watered_without', 'تسقى بدون تكلفة'),
    ]    
    user = models.ForeignKey(User, on_delete=models.CASCADE)    
    zakat_type = models.ForeignKey(ZakatType, on_delete=models.CASCADE)
    Irrigation_method = models.CharField(max_length=20, choices=IRRIGATION_METHOD)    
    Plants_per_kilo=models.DecimalField(max_digits=20, decimal_places=3)
    amount = models.DecimalField(max_digits=20, decimal_places=3)
    zakatWeight= models.DecimalField(max_digits=20, decimal_places=3)
    year_harvested = models.DateField()  # تاريخ الحصاد
    Price_per_kilo=models.DecimalField(max_digits=20, decimal_places=3)
    def __str__(self):
        return f"{self.user.username} {self.amount}"