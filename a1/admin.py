from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display=('id','title','img','description','created_at',)
    list_filter = ('id', 'created_at',)
    search_fields = ("id",)
    list_editable=('title','description',)
admin.site.register(Product,ProductAdmin)