from django.shortcuts import redirect, render, reverse
from django.views.generic import View, CreateView

# models
from member.models import Member, MemberProfile

# forms
from authentication.forms import (
    RegisterForm,
    LoginForm,
)

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages


class RegisterView(View):
    def get(self, request):

        signed_in_member = request.user
        template_name = "generic_form.html"
        form = RegisterForm()
        context = {"signed_in_member": signed_in_member, "form": form, "header": "Register"}

        return render(request, template_name, context)

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            member = Member.objects.create_user(
                username=data.get("username"),
                password=data.get("password"),
            )

            try:
                messages.add_message(request, messages.SUCCESS, f"Login Successful")
                login(request, member)
                return redirect("createprofile")
            except Exception as ex:
                messages.add_message(request, messages.ERROR, f"Login Invalid")
                print("Something went wrong….", ex)
                return redirect(reverse("login"))


class LoginView(View):
    def get(self, request):

        signed_in_member = request.user
        template_name = "generic_form.html"
        form = LoginForm()
        context = {"form": form, "header": "Login", "signed_in_member": signed_in_member}
        return render(request, template_name, context)

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            logged_in_user = authenticate(
                request, username=data.get("username"), password=data.get("password")
            )
            if logged_in_user:
                login(request, logged_in_user)
                messages.add_message(
                    request,
                    message="You have successfully logged in.",
                    level=messages.SUCCESS,
                )
                return redirect(reverse("home"))
            if logged_in_user is not None:
                login(request, logged_in_user)
                return redirect(reverse("generic_form.html"))
        else:
            messages.add_message(
                request,
                message="Credentials Invalid",
                level=messages.ERROR,
            )
            return redirect(reverse("login"))


def logout_view(request):
    logout(request)
    messages.add_message(
        request, message="You have sucessfully logged out.", level=messages.INFO
    )
    return redirect("/")
