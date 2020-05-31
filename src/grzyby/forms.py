from django import forms  
from grzyby.models import grzyb



class GrzybForm(forms.ModelForm):  
    class Meta:  
        model = grzyb
        fields = "__all__"  