from django import forms
from .models import Product
import re

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"
        
        error_messages = {
            "name": {
                "max_length": "O tamanho máximo do nome é 255 caracteres",
            }
        }
        
    # clean_<nome_campo>
    def clean_sale_price(self):
        # Obtendo o valor que foi digitado no formulário
        sale_price = self.cleaned_data.get("sale_price", "")
        
        # Removendo valores não numéricos
        sale_price = re.sub("[^0-9,.]", "", sale_price)
        
        return sale_price
