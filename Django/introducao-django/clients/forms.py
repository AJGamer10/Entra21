from django.forms import ModelForm
from .models import Client

class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = ["nome", "email", "cpf", "zipcode", "phone", "street", "city", "state", "enabled"]