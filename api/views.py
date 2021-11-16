from django.shortcuts import redirect, render, reverse
from django.views.generic import View, CreateView

# models
from authentication.models import User, Profile

# forms
from authentication.forms import (
    RegisterForm,
    LoginForm,
    CreateProfileForm,
    EditProfileForm
)

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages


class Dashboard(View):
    '''private view for users to look upp cryptos
    and be able to save them and track their gains
    and losses
    '''
    def get(self, request):
        pass

    def post(self, request):
        pass

class SearchCrypto(View):
    '''search and view cryptos'''
    def get(self, request):
        pass

    def post(self, request):
        pass
