from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(
        label="Username", 
        max_length=200, 
        widget=forms.TextInput(attrs={'class': 'input'})
    )
    password = forms.CharField(
        label="Password", 
        max_length=200, 
        widget=forms.PasswordInput(attrs={'class': 'input'})
    )


class CreateNewUser(forms.Form):
    username = forms.CharField(
        label="Username", 
        max_length=200, 
        widget=forms.TextInput(attrs={'class': 'input'})
    )
    password = forms.CharField(
        label="Password", 
        max_length=200, 
        widget=forms.PasswordInput(attrs={'class': 'input'})
    )
    confirm_password = forms.CharField(
        label="Confirm Password", 
        max_length=200, 
        widget=forms.PasswordInput(attrs={'class': 'input'})
    )
