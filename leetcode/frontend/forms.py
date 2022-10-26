from django import forms
from .models import Code


class CodeForm(forms.ModelForm):

    class Meta:
        model = Code
        fields = ('title', 'program')
        widget = {
            'program': forms.Textarea(),
        }
