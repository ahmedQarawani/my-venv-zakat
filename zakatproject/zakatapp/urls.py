from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/signup/', views.signup, name='signup'),
    path('accounts/login/', views.user_login, name='login'),
    path('accounts/logout/', views.logout_view, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('zakatCalculator/gold/', views.calculate_gold_zakat, name='calculate_gold_zakat'),
    path('zakatCalculator/silver/', views.calculate_silver_zakat, name='calculate_silver_zakat'),
    path('zakatCalculator/money/', views.calculate_money_zakat, name='calculate_money_zakat'),
    path('zakatCalculator/plant/', views.calculate_plant_zakat, name='calculate_plant_zakat'),
    path('zakatCalculator/livestock/', views.calculate_livestock_zakat, name='calculate_livestock_zakat'),

]
