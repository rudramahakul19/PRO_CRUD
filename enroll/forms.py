from django import forms
from .models import User


class StudentRegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email','mobile', 'password']
        widgets ={
            'password': forms.PasswordInput(render_value=True ,attrs={'class':'form-control'}),
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'mobile': forms.TextInput(attrs={'class':'form-control'}),
                  }