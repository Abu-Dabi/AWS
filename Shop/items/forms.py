from django import forms


class UserLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form.control'}))
    password = forms.CharField(widget=forms.TextInput(attrs={'class': 'form.control'}))

