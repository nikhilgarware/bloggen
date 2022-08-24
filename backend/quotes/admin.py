from django.contrib import admin
from quotes.models import Quotes
# Register your models here.


class QuotesAdmin(admin.ModelAdmin):
    list_display = ('quote', 'genre')


admin.site.register(Quotes, QuotesAdmin)
