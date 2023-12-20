from django.contrib import admin
from pages.models import *

# Register your models here.

# @admin.register(MainScrollModel)
# class ModelNameAdmin(admin.ModelAdmin):
#     list_display = ['title', 'discount', 'created_at', 'updated_at']
#     search_fields = ['title', 'info']
#     list_filter = ['created_at', 'updated_at']



# @admin.register(Menu)
# class Home_menu(admin.ModelAdmin):
#     list_display = ['title', 'discount']
#     search_fields = ['title', 'info']


admin.site.register(MainScrollModel)
admin.site.register(Menu)