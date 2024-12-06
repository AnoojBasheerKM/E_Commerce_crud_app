from django import forms

from django.contrib.auth.forms import UserCreationForm

from store.models import User,Order


class SignUpForm(UserCreationForm):
    
    class Meta:
        
        model = User
        
        fields = ["username","email","phone","password1","password2",]
        
class LoginForm(forms.Form):
    
    username = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))
    
class orderForm(forms.ModelForm):
    
    class Meta:
        
        model =  Order
        
        fields = ["address","phone","payment_method"]  

        

        