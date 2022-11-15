from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# class NewUserForm(UserCreationForm):
#     email = forms.EmailField(required=True)

#     class Meta:
#         model = User
#         fields = ("username", "email", "password1", "password2")

#     def save(self, commit=True):
#         user = super(NewUserForm, self).save(commit=False)
#         user.email = self.cleaned_data["email"]
#         if commit:
#             user.save()
#         return user

class Item_form(forms.ModelForm):
    Name=forms.CharField(widget=forms.TextInput(attrs={"class":"w-full px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm focus:outline-none focus:border-gray-400 focus:bg-white mt-5","placeholder":"Item name"}))
    Cost=forms.IntegerField(widget=forms. NumberInput(attrs={"class":"w-full px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm focus:outline-none focus:border-gray-400 focus:bg-white mt-5","placeholder":"Price"}))
    Upload=forms.ImageField(widget=forms.FileInput(attrs={"class":"w-full px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm focus:outline-none focus:border-gray-400 focus:bg-white mt-5","placeholder":"Upload image"}))
    Description=forms.CharField(widget=forms.TextInput(attrs={"class":"w-full px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm focus:outline-none focus:border-gray-400 focus:bg-white mt-5","placeholder":"Add description"}))
    class Meta:
        model = items_data
        fields = ['Name','Cost','Upload','Description']
        
class CreateUserForm(UserCreationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"w-full px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm focus:outline-none focus:border-gray-400 focus:bg-white mt-5","placeholder":"Username"}))
    first_name=forms.CharField(widget=forms.TextInput(attrs={"class":"w-full px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm focus:outline-none focus:border-gray-400 focus:bg-white mt-5","placeholder":"Firstname"}))
    last_name=forms.CharField(widget=forms.TextInput(attrs={"class":"w-full px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm focus:outline-none focus:border-gray-400 focus:bg-white mt-5","placeholder":"Lastname"}))
    email=forms.CharField(widget=forms.EmailInput(attrs={"class":"w-full px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm focus:outline-none focus:border-gray-400 focus:bg-white mt-5","placeholder":"E-mail"}))
    password1=forms.CharField(widget=forms.PasswordInput(attrs={"class":"w-full px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm focus:outline-none focus:border-gray-400 focus:bg-white mt-5","placeholder":"Password"}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={"class":"w-full px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm focus:outline-none focus:border-gray-400 focus:bg-white mt-5","placeholder":"Password check"}))
    
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2']