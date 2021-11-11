from django.forms import ModelForm, CheckboxInput, NumberInput, RadioSelect
from .models import FilterComics


class FilterComicsForm(ModelForm):
    class Meta:
        model = FilterComics
        fields = ['marvel', 'dc', 'bubble', 'dark_horse', 'other', 'mark']
        widgets = {
            'mark': NumberInput(attrs={
                'type': "number",
                'size': "1",
                'name':  "num",
                'min': 1,
                'max': 5,
                'value': "1",
        }),
            'marvel': CheckboxInput(attrs={
                'class': "form-check-input",
            }),
            'dc': CheckboxInput(attrs={
                'class': "form-check-input",
            }),
            'dark_horse': CheckboxInput(attrs={
                'class': "form-check-input",
            }),
            'bubble': CheckboxInput(attrs={
                'class': "form-check-input"
            }),
            'other': CheckboxInput(attrs={
                'class': "form-check-input",
            })
        }