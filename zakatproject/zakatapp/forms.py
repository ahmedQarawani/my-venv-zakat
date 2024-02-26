from django import forms
from django.forms.widgets import DateInput
from django.utils import timezone
from django import forms

class GoldZakatForm(forms.Form):
    GOLD_KARAT = [
        ('24', '24'),
        ('22', '22'),
        ('21', '21'),
        ('18', '18'),
        ('14', '14'),
    ]
    year_type = forms.ChoiceField(choices=[('M', 'ميلادي'), ('H', 'هجري')],label='نوع الحول')
    weight = forms.DecimalField(max_digits=10, decimal_places=2,max_value=9999999999.99,label='وزن الذهب  ')
    gold_karat = forms.ChoiceField(choices=GOLD_KARAT,label='وزن الذهب عيار ')
    Price_of_gram_of_gold =forms.DecimalField(max_digits=15, decimal_places=2,max_value=999999999999999.99,label='سعر غرام الذهب')

    
class SilverZakatForm(forms.Form):
    year_type = forms.ChoiceField(choices=[('M', 'ميلادي'), ('H', 'هجري')],label='نوع الحول')
    weight = forms.DecimalField(max_digits=10, decimal_places=2,max_value=9999999999.99,label='وزن الفضة  ')
    Price_of_gram_of_silver=forms.DecimalField(max_digits=15, decimal_places=2,max_value=999999999999999.99,label='سعر غرام الفضة')
    
class MoneyZakatForm(forms.Form):
    year_type = forms.ChoiceField(choices=[('M', 'ميلادي'), ('H', 'هجري')],label='نوع الحول')
    silver_price = forms.DecimalField(max_digits=15, decimal_places=2,max_value=999999999999999.99,label='سعر غرام الفضة')
    money=forms.DecimalField(max_digits=15, decimal_places=3,max_value=999999999999999.99,label='المبلغ')
    
class LivestockZakatForm(forms.Form):
    ANIMAL_TYPES = [
        ('C', 'بقرة'),
        ('S', 'شاة'),
        ('G', 'ابل'),
    ]
    YESORNO=[
        ('yes','نعم'),
        ('no','لا')
    ]
    animal_type = forms.ChoiceField(choices=ANIMAL_TYPES,label='نوع الماشية')
    not_expensive=forms.ChoiceField(choices=YESORNO,label='هل هي سائمه(لا نتكلف بالطعام الخاص بها ترعى العشب الذي ينبت وحده)')
    lunar_strabismus=forms.ChoiceField(choices=YESORNO,label='هل هي للنسل والدر (اي للانتاج والتكاثر)')
    reproduction_and_production=forms.ChoiceField(choices=YESORNO,label='هل مضي على امتلاكها حول قمري كامل')
    count = forms.IntegerField(max_value=999999999999,label='العدد')
    
class PlantZakatForm(forms.Form):
    Plants_per_kilo = forms.DecimalField(max_digits=15, decimal_places=2,max_value=999999999999999.99,label='عدد الكيلو غرامات التي تمتلكها')
    Price_per_kilo = forms.DecimalField(max_digits=10, decimal_places=2,max_value=9999999999.99,label='سعر الكيلو جرام الواحد')
    Irrigation_method = forms.ChoiceField(choices=[('Watering_at_a_cost', 'تسقى بتكلفه'), ('Watered_without', 'تسقى بدون تكلفة')],label='طريقة الري')
    year_harvested = forms.DateTimeField(widget=DateInput(attrs={'type': 'date'}), initial=timezone.now,label='تاريخ الحصاد')
    
