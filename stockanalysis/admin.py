from django.contrib import admin
from .models import Stock, StockData

class Stockdmin(admin.ModelAdmin):
    search_fields = ('id', 'name', 'symbol')

admin.site.register(Stock)
admin.site.register(StockData)
