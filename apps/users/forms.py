from django import forms

class LoginForm(forms.Form):
    login_name = forms.CharField(
        label="Nome de usuário",
        required=True,
        max_length=100,
        widget = forms.TextInput(
            attrs={
                "class": "user-form-input"
            }
        )
    )

    password = forms.CharField(
        label="Senha",
        required=True,
        widget = forms.PasswordInput(
            attrs={
                "class": "user-form-input"
            }
        )
    )

class SignUpForm(forms.Form):
    sign_up_name = forms.CharField(
        label="Nome de usuário",
        required=True,
        max_length=100,
        widget = forms.TextInput(
            attrs={
                "class": "user-form-input"
            }
        )
    )

    password_1 = forms.CharField(
        label="Senha",
        required=True,
        widget = forms.PasswordInput(
            attrs={
                "class": "user-form-input"
            }
        )
    )

    password_2 = forms.CharField(
        label="Confirme a Senha",
        required=True,
        widget = forms.PasswordInput(
            attrs={
                "class": "user-form-input"
            }
        )
    )
