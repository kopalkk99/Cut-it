from UrlShortner.models import ShortUrl
from django import forms

class ShortUrlForm(forms.ModelForm):

    class Meta():
        fields = {'original_url'}
        model = ShortUrl

        widgets = {
            'original_url' : forms.TextInput(attrs={'class':'form-control'})
        }
