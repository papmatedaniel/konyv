from django import forms
from .models import Konyvek

class KonyvekForm(forms.ModelForm):  # Az osztály neve is egyezzen
    class Meta:
        model = Konyvek  # Ezt a modelledet kell használni
        fields = '__all__'
