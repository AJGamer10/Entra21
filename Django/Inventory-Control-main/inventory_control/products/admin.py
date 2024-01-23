from django.contrib import admin
from .models import Product

# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "description", "photo", "enabled"]
    exclude = ["slug"]
    ordering = ["-id"]
    list_filter = ["enabled"]
    search_fields = ["name"]
    list_display_links = ["name"]
    list_editable = ["description", "photo", "enabled"]
    list_per_page = 20
    list_max_show_all = 1000
