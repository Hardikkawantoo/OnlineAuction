from django.contrib import admin
from app1.models import items_data

class Indexing(admin.ModelAdmin):
    readonly_fields=('id',)

# Register your models here.

admin.site.register(items_data,Indexing)

