from django import forms

class LoginForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        label='Nome de login',
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ex.: Enya, Takai ...'
            }
        )
    )

    password = forms.CharField(
        max_length=70,
        label='Senha',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite sua senha'
            }
        )
    )

