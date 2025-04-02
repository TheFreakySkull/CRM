from django import forms

class LoginForm(forms.Form):
    login = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'exampleInputEmail1', 'aria-describedby': 'emailHelp'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'type': 'password', 'class': 'form-control', 'id': 'exampleInputPassword1'}), max_length=25)

class CreateUserForm(forms.Form):
    username = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'user', 'aria-describedby': 'emailHelp', 'placeholder': 'Обязательное поле'}))
    password = forms.CharField(max_length=25, widget=forms.PasswordInput(attrs={'type': 'password', 'class': 'form-control', 'id': 'password', 'placeholder': 'Обязательное поле'}))
    email = forms.EmailField(max_length=45, widget=forms.EmailInput(attrs={'class': 'form-control', 'id': 'email', 'aria-describedby': 'emailHelp'}))
    is_superuser = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-check-input form-switch', 'type': 'checkbox', 'id': 'fixedcheckbox'}), required=False)
