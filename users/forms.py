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


class RegisterForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        label='Nome',
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ex.: Enya, Takai ...'
            }
        )
    )

    email = forms.EmailField(
        max_length=100,
        label='Email',
        required=True,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ex.: enya@email.com ...'
            }
        )
    )

    password_1 = forms.CharField(
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

    password_2 = forms.CharField(
        max_length=70,
        label='Confirme sua senha',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite sua senha novamente'
            }
        )
    )

    # validated only the name field
    def clean_name(self):
        name = self.cleaned_data.get('name')

        if name:
            name = name.strip()

            if ' ' in name:
                raise forms.ValidationError(
                    'Não é possível inserir espaços dentro do campo nome')

        return name
