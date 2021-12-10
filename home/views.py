from django.shortcuts import redirect, render, reverse
from django.views.generic import View, CreateView

# models
from member.models import Member, MemberProfile


from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages


class IndexView(View):
    """index page upon coming to site"""

    def get(self, request):

        signed_in_user = request.user
        template = "index.html"
        context = {"signed_in_user": signed_in_user}
        return render(request, template, context)

    def post(self, request):
        ...


class HomeView(View, LoginRequiredMixin):
    """index page upon coming to site"""

    def get(self, request):

        signed_in_user = request.user
        template = "home.html"
        context = {"signed_in_user": signed_in_user}
        return render(request, template, context)

    def post(self, request):
        ...


def about(request):
    template = "about.html"
    signed_in_user = request.user
    context = {"signed_in_user": signed_in_user}
    return render(request, template, context)
