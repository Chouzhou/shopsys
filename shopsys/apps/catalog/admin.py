#-*- coding:utf-8 -*-
from django.contrib import admin
from .models import Category,Product
from .forms import ProductAdminForm
# Register your models here.
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
'''
加这段代码的原因是防止出现这样的错误
'ascii' codec can't encode characters in position 0-1:
    ordinal not in range(128)
'''
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    form = ProductAdminForm
    #设置admin界面如何显示产品列表
    list_display = ('name','price','old_price','created_at','updated_at',)
    list_display_links = ('name',)
    list_per_page = 50
    ordering = ['-created_at']
    search_fields = ['name','description','meta_keywords','meta_description']
    exclude = ('created_at','updated_at',)
    prepopulated_fields = {'slug' : ('name',)}

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','created_at','updated_at',)
    list_display_links = ('name',)
    list_per_page = 20
    ordering = ['name']
    search_fileds = ['name','description','meta_keywords','meta_description']
    exclude = ('created_at','updated_at',)
    prepopulated_fields = {'slug':('name',)}


