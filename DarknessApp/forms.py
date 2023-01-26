from django import forms
from DarknessApp.models import text123,comment1

class text1(forms.ModelForm):
    class Meta:
        model=text123
        fields="__all__"
class Text2(forms.ModelForm):
    class Meta:
        model=comment1
        fields="__all__"