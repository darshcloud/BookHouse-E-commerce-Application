from socket import fromshare
from django import forms
from .models import Account

class RegistrationForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput(attrs={
    'placeholder':'enter password',
    'class': 'form-control',
    }))
    confirm_password=forms.CharField(widget=forms.PasswordInput(attrs={
    'placeholder':'repeat password',
    'class': 'form-control',
    }))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    phone_number = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    

    class Meta:
        model=Account
        fields=['first_name','last_name','phone_number','email','password']

    # def __int__(self,*args,**kwargs):
    #     super(RegistrationForm, self).__init__(*args,**kwargs)
    #     for field in self.fields:
    #         self.fields[field].widget.attrs['class']= 'form-control'

    def clean(self):
        cleaned_data = super(RegistrationForm,self).clean()
        password=cleaned_data.get('password')
        confirm_password=cleaned_data.get('confirm_password')

        if password!= confirm_password:
            raise forms.ValidationError(
                "Password does not match!"
            )





