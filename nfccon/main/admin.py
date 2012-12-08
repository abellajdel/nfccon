from django.contrib import admin
from main.models import *

class NfcTagAdmin(admin.ModelAdmin):
    list_display = ('id', 'item')


class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'item_type')


class ItemTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


admin.site.register(NfcTag, NfcTagAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(ItemType, ItemTypeAdmin)
