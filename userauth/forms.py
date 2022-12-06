# from django import forms
# from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm

# class UserCreateForm(UserCreationForm):
#     bloodgroup = forms.CharField(required=True)
#     address = forms.CharField(required=True)
#     clas = forms.CharField(required=True)
#     name = forms.CharField(required=True)

#     class Meta:
#         model = User
#         fields = ("username", "password1", "password2", "name", "bloodgroup", "address", "clas")

#     def save(self, commit=True):
#         user = super(UserCreateForm, self).save(commit=False)
#         user.bloodgrp = self.cleaned_data["bloodgroup"]
#         user.addr = self.cleaned_data["address"]
#         user.cls = self.cleaned_data["clas"]
#         user.name = self.cleaned_data["name"]
#         if commit:
#             user.save()
#         return user