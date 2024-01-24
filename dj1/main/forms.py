from .models import mainbd
from django.forms import ModelForm, TextInput, Textarea

class mainbdForm(ModelForm):
    class Meta:
        model = mainbd
        fields=['name','text']

        widgets={
            'name':TextInput(attrs={
            'class': 'form',
            'placeholder': 'дай имя'
            }),
            'text': Textarea(attrs={
                'class': 'form',
                'placeholder': 'дай погоняло'
            })
        }