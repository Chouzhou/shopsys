#-*- coding:utf-8 -*-

from django import forms
from .models import Product
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
'''
 加这段代码的原因是防止出现以下错误
'ascii' codec can't encode characters in position 0-1:
    ordinal not in range(128)
'''
class ProductAdminForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = []#必须写不然会报错


    def clean_price(self):
        if self.cleaned_data['price'] <= 0:
            raise forms.ValidationError('价格必须大于0.')
        return self.cleaned_data['price']
