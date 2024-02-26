from django.contrib import admin

from .models import ZakatType,GoldZakat,SilverZakat,UserProfile,MoneyZakat,PlantZakat,LivestockZakat

admin.site.register(GoldZakat)
admin.site.register(ZakatType)
admin.site.register(SilverZakat)
admin.site.register(UserProfile)
admin.site.register(MoneyZakat)
admin.site.register(PlantZakat)
admin.site.register(LivestockZakat)