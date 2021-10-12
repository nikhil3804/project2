from django import forms
class f1(forms.Form):
    login=forms.CharField()
    password=forms.CharField()


class registerForm(forms.Form):
    name=forms.CharField()
    email=forms.CharField()
    password=forms.CharField()