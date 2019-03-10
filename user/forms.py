from django import forms


class loginForm(forms.Form):
    username = forms.CharField(required=True, max_length=25)
    password = forms.CharField(required=True, max_length=30)
