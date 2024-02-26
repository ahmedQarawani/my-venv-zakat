from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, HttpResponse
from django.http import HttpResponse
from django.urls import reverse
from .models import GoldZakat, MoneyZakat, SilverZakat,PlantZakat,ZakatType,LivestockZakat
from .forms import GoldZakatForm,SilverZakatForm,MoneyZakatForm,PlantZakatForm,LivestockZakatForm
from decimal import Decimal, InvalidOperation
from datetime import date,datetime

#--------Beginning of calculating gold zakat--------
@login_required
def calculate_gold_zakat(request):
    if request.method == 'POST':
        form = GoldZakatForm(request.POST)
        if form.is_valid():
            weight = form.cleaned_data.get('weight')
            gold_karat = form.cleaned_data.get('gold_karat')
            year_type = form.cleaned_data.get('year_type')
            price_of_gram_of_gold = form.cleaned_data.get('Price_of_gram_of_gold')
            user = request.user
            if weight < 0 or price_of_gram_of_gold < 0:
                return HttpResponse("الرجاء إدخال قيم غير سالبة")
        try:
            if year_type == 'H':
                if weight < 85:
                    return HttpResponse("لا زكاة عليك")
                weight_decimal = Decimal(str(weight)) 
                if gold_karat == '24':
                    zakat_amount = (Decimal('0.025') * weight_decimal) * price_of_gram_of_gold
                elif gold_karat == '22':
                    new_karat = (22 * weight_decimal) / 24
                    if new_karat < 85:
                        return HttpResponse("لا زكاة عليك")
                    zakat_amount = (Decimal('0.025') * new_karat) * price_of_gram_of_gold                     
                elif gold_karat == '21':
                    new_karat = (21 * weight_decimal) / 24
                    if new_karat < 85:
                        return HttpResponse("لا زكاة عليك")
                    zakat_amount = (Decimal('0.025') * new_karat) * price_of_gram_of_gold                     
                elif gold_karat == '18':
                    new_karat = (18 * weight_decimal) / 24
                    if new_karat < 85:
                        return HttpResponse("لا زكاة عليك")
                    zakat_amount = (Decimal('0.025') * new_karat) * price_of_gram_of_gold                     
                elif gold_karat == '14':
                    new_karat = (14 * weight_decimal) / 24
                    if new_karat < 85:
                        return HttpResponse("لا زكاة عليك")
                    zakat_amount = (Decimal('0.025') * new_karat) * price_of_gram_of_gold                     
                else:
                    return HttpResponse("عيار ذهب غير صالح")
            elif year_type == 'M':
                if weight < 85:
                    return HttpResponse("لا زكاة عليك")
                weight_decimal = Decimal(str(weight)) 
                if gold_karat == '24':
                    zakat_amount = (Decimal('0.025775') * weight_decimal) * price_of_gram_of_gold
                elif gold_karat == '22':
                    new_karat = (22 * weight_decimal) / 24
                    if new_karat < 85:
                        return HttpResponse("لا زكاة عليك")
                    zakat_amount = (Decimal('0.025775') * new_karat) * price_of_gram_of_gold
                elif gold_karat == '21':
                    new_karat = (21 * weight_decimal) / 24
                    if new_karat < 85:
                        return HttpResponse("لا زكاة عليك")
                    zakat_amount = (Decimal('0.025775') * new_karat) * price_of_gram_of_gold
                elif gold_karat == '18':
                    new_karat = (18 * weight_decimal) / 24
                    if new_karat < 85:
                        return HttpResponse("لا زكاة عليك")
                    zakat_amount = (Decimal('0.025775') * new_karat) * price_of_gram_of_gold
                elif gold_karat == '14':
                    new_karat = (14 * weight_decimal) / 24
                    if new_karat < 85:
                        return HttpResponse("لا زكاة عليك")
                    zakat_amount = (Decimal('0.025775') * new_karat) * price_of_gram_of_gold
                else:
                    return HttpResponse("عيار ذهب غير صالح")                
                pass
            else:
                return HttpResponse("نوع السنة غير صالح")
            
            zakat_type, created = ZakatType.objects.get_or_create(zakat_typee='gold')
            gold_zakat = GoldZakat.objects.create(user=user, weight=weight, gold_karat=gold_karat, amount=zakat_amount, zakat_type=zakat_type, year_type=year_type, Price_of_gram_of_gold=price_of_gram_of_gold)
            calculate_gold_zakat_url = reverse('calculate_gold_zakat')
            response = "تم حساب الزكاة بنجاح: {}.<br>هل ترغب في حساب زكاة أخرى؟ <a href='{}'>نعم</a>".format(zakat_amount, calculate_gold_zakat_url)
            return HttpResponse(response)
        except InvalidOperation:
            return HttpResponse("خطأ في العملية الحسابية")        
    else:
        form = GoldZakatForm()
        return render(request, 'zakatCalculator/calculate_gold_zakat.html', {'form': form})
#--------End of gold zakat calculation--------


#--------Beginning of calculating Silver zakat--------
@login_required
def calculate_silver_zakat(request):
    if request.method == 'POST':
        form = SilverZakatForm(request.POST)
        if form.is_valid():
            year_type = form.cleaned_data.get('year_type')
            weight = form.cleaned_data.get('weight')
            price_of_gram_of_silver = form.cleaned_data.get('Price_of_gram_of_silver')
            user = request.user
            if weight < 0 or price_of_gram_of_silver < 0:
                return HttpResponse("الرجاء إدخال قيم غير سالبة")
        try:
            if year_type=='H':
                if weight<595:
                    return HttpResponse("لا زكاة عليك")
                weight_decimal = Decimal(str(weight)) 
                zakat_amount = (Decimal('0.025') * weight_decimal) * price_of_gram_of_silver
                
            elif year_type == 'M':
                if weight < 595:
                    return HttpResponse("لا زكاة عليك")
                weight_decimal = Decimal(str(weight)) 
                zakat_amount = (Decimal('0.025775') * weight_decimal) * price_of_gram_of_silver        
            else:
                return HttpResponse("نوع السنة غير صالح")     
            zakat_type, created = ZakatType.objects.get_or_create(zakat_typee='silver')
            silverZakat = SilverZakat.objects.create(user=user, weight=weight, amount=zakat_amount, zakat_type=zakat_type, year_type=year_type, Price_of_gram_of_silver=price_of_gram_of_silver)
            calculate_silver_zakat_url = reverse('calculate_silver_zakat')
            response = "تم حساب الزكاة بنجاح: {}.<br>هل ترغب في حساب زكاة أخرى؟ <a href='{}'>نعم</a>".format(zakat_amount, calculate_silver_zakat_url)
            return HttpResponse(response)
        except InvalidOperation:
            return HttpResponse("خطأ في العملية الحسابية")   
    else:
        form = SilverZakatForm()
        return render(request, 'zakatCalculator/calculate_silver_zakat.html', {'form': form})                              
#--------End of Silver zakat calculation--------


#--------Beginning of calculating money zakat--------
@login_required
def calculate_money_zakat(request):
    if request.method == 'POST':
        form = MoneyZakatForm(request.POST)
        if form.is_valid():
            year_type = form.cleaned_data.get('year_type')
            silver_price = form.cleaned_data.get('silver_price')
            money = form.cleaned_data.get('money')
            user = request.user
            if silver_price < 0 or money < 0:
                return HttpResponse("الرجاء إدخال قيم غير سالبة")
            
            try:
                if year_type == 'H':
                    silver_weight = money / silver_price
                    if silver_weight < 595:
                        return HttpResponse("لا زكاة عليك")
                    zakat_amount = (Decimal('0.025') * silver_weight) * silver_price
                elif year_type == 'M':
                    if money < 595:
                        return HttpResponse("لا زكاة عليك")
                    zakat_amount = (Decimal('0.025775') * silver_price)
                else:
                    return HttpResponse("نوع السنة غير صالح") 
                
                zakat_type, created = ZakatType.objects.get_or_create(zakat_typee='money')
                money_zakat = MoneyZakat.objects.create(user=user, silver_price=silver_price, amount=zakat_amount, zakat_type=zakat_type, year_type=year_type, money=money)
                calculate_money_zakat_url = reverse('calculate_money_zakat')
                response = "تم حساب الزكاة بنجاح: {}.<br>هل ترغب في حساب زكاة أخرى؟ <a href='{}'>نعم</a>".format(zakat_amount, calculate_money_zakat_url)
                return HttpResponse(response)            
            except InvalidOperation:
                return HttpResponse("خطأ في العملية الحسابية")
    else:
        form = MoneyZakatForm()
        return render(request, 'zakatCalculator/calculate_money_zakat.html', {'form': form}) 

#--------End of money zakat calculation--------

#--------Beginning of calculate livestock zakat--------
@login_required
def calculate_livestock_zakat(request):
    if request.method == 'POST':
        form = LivestockZakatForm(request.POST)
        if form.is_valid():
            animal_type = form.cleaned_data.get('animal_type')
            not_expensive = form.cleaned_data.get('not_expensive')
            lunar_strabismus = form.cleaned_data.get('lunar_strabismus')
            reproduction_and_production = form.cleaned_data.get('reproduction_and_production')
            count = form.cleaned_data.get('count')
            user = request.user
            
            if not_expensive == 'no':
                return HttpResponse('لا زكاه عليك')
            if lunar_strabismus == 'no':
                return HttpResponse('لا زكاه عليك')
            if reproduction_and_production == 'no':
                return HttpResponse('لا زكاه عليك')
            
            if animal_type == 'C':
                if count < 30:
                    return HttpResponse('لا زكاه عليك')
                zakat_count = count // 30  
            elif animal_type == 'S':
                if count < 40:
                    return HttpResponse('لا زكاه عليك')
                zakat_count = count // 40  
            elif animal_type == 'G':
                if count < 5:
                    return HttpResponse('لا زكاه عليك')
                zakat_count = count // 5
            else:
                return HttpResponse('نوع الزكاه من المواشي غير موجود')
            
            
            livestock_zakat = LivestockZakat.objects.create(
                user=user,
                animal_type=animal_type,
                count=count,
                amount=zakat_count  
            )
            return HttpResponse(f'الزكاة الواجبة عليك من الانعام: {zakat_count}')
    else:
        form = LivestockZakatForm()
    return render(request, 'zakatCalculator/calculate_livestock_zakat.html', {'form': form})
#--------End of livestock zakat calculation--------


#--------Beginning of calculate plant zakat--------
@login_required
def calculate_plant_zakat(request):
    if request.method == 'POST':
        form = PlantZakatForm(request.POST)
        if form.is_valid():
            Plants_per_kilo = form.cleaned_data.get('Plants_per_kilo')
            Price_per_kilo = form.cleaned_data.get('Price_per_kilo')
            Irrigation_method = form.cleaned_data.get('Irrigation_method')
            year_harvested = form.cleaned_data.get('year_harvested')
            user = request.user
            if Plants_per_kilo < 0 or Price_per_kilo < 0:
                return HttpResponse("الرجاء إدخال قيم غير سالبة")
            
            if isinstance(year_harvested, datetime):
                year_harvested = year_harvested.date()
            if year_harvested > date.today():
                return HttpResponse("تاريخ الحرث لا يمكن أن يكون في المستقبل")
        try:
            if Plants_per_kilo<653:
                return HttpResponse('لا زكاة عليك')
            if Irrigation_method=='Watering_at_a_cost':
                zakatWeight=(Decimal('0.05') * Plants_per_kilo)
                zakat_amount = zakatWeight * Price_per_kilo 
            elif Irrigation_method =='Watered_without':
                zakatWeight=(Decimal('0.05') * Plants_per_kilo)
                zakat_amount = zakatWeight * Price_per_kilo            
            else:
                return HttpResponse('نوع الري غير صالح') 
            zakat_type, created = ZakatType.objects.get_or_create(zakat_typee='plant')
            plant_zakat = PlantZakat.objects.create(user=user, amount=zakat_amount,Plants_per_kilo=Plants_per_kilo,Price_per_kilo=Price_per_kilo,Irrigation_method=Irrigation_method,year_harvested=year_harvested,zakat_type=zakat_type,zakatWeight=zakatWeight)
            calculate_plant_zakat_url = reverse('calculate_plant_zakat')
            response = "تم حساب الزكاة بنجاح: {} كيلو غرام, بمبلغ {}.<br>هل ترغب في حساب زكاة أخرى؟ <a href='{}'>نعم</a>".format(zakatWeight, zakat_amount, calculate_plant_zakat_url)
            return HttpResponse(response)
        except InvalidOperation:
            return HttpResponse("خطأ في العملية الحسابية")
    else:
        form = PlantZakatForm()
        return render(request, 'zakatCalculator/calculate_plant_zakat.html', {'form': form})           
    #--------End of plant zakat calculation--------
    
                   
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

def profile(request):
    gold_zakats = GoldZakat.objects.filter(user=request.user)
    money_zakats = MoneyZakat.objects.filter(user=request.user)
    silver_zakats = SilverZakat.objects.filter(user=request.user)
    plant_zakats=PlantZakat.objects.filter(user=request.user)
    return render(request, 'profile.html', {'gold_zakats': gold_zakats, 
                                             'money_zakats': money_zakats, 
                                             'silver_zakats': silver_zakats,
                                             'plant_zakats': plant_zakats,
                                             })

@login_required
def home(request):
    return render(request, 'home.html')

def logout_view(request):
    logout(request)
    return redirect(reverse('home'))