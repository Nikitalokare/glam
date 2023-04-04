from django import forms

class MyFileForm(forms.Form):
    file_name=forms.FileField(widget=forms.FileInput(attrs={'class':'form-control'}))