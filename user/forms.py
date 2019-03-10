from django import forms


class loginForm(forms.Form):
    username = forms.CharField(required=True, max_length=25)
    password = forms.CharField(required=True, max_length=30)


class signupForm(forms.Form):
    username = forms.CharField(required=True, max_length=25)
    email = forms.EmailField(required=False, max_length=75)
    password = forms.CharField(required=True, max_length=30)
