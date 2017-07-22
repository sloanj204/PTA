from django import forms
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404


# def user_list():
#     users = User.objects.all()
#     users = [(u.id, u.username) for u in users if not u.is_staff]
#     return users
#
#
# class UserChooseForm(forms.Form):
#     choose_user = forms.ChoiceField(choices=user_list())
#
#
# class UserEditForm(forms.Form):
#     user_name = forms.CharField(label="Username")
#     password = forms.CharField(label="Password")
#     first_name = forms.CharField(label="First Name")
#     last_name = forms.CharField(label="Last Name", required=False)
#     email = forms.CharField(label="Email address")



