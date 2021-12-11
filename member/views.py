from django.shortcuts import redirect, render, reverse
from django.views.generic import View, CreateView

# models
from member.models import Member, MemberProfile

# forms
from member.forms import (
    CreateProfileForm,
    EditProfileForm,
)

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages


class MemberView(View):
    """each users profile"""

    def get(self, request, id):

        signed_in_member = request.user
        target_member = Member.objects.get(id=id)
        print(target_member)

        try:
            profile = MemberProfile.objects.get(member=target_member)
        except Exception as err:
            print(err)
            profile = None
        # print(f"Picture: {target_member.profile_picture}")

        template = "profile.html"

        # breakpoint()
        print(target_member)
        context = {
            "signed_in_member": signed_in_member,
            "target_member": target_member,
            "profile": profile,
        }
        return render(request, template, context)

    def post(self, request):
        ...


class CreateProfileView(View):
    """create a profile upon signing up"""

    def get(self, request):

        form = CreateProfileForm()
        template = "generic_form.html"
        context = {"form": form, "header": "Create Your Profile"}
        return render(request, template, context)

    def post(self, request):

        target_member = Member.objects.get(id=request.user.id)

        form = CreateProfileForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data

            profile = MemberProfile.objects.create(
                member=target_member,
                first_name=data["first_name"],
                last_name=data["last_name"],
                # email=data["email"],
                profile_picture=data["profile_picture"],
                bio=data["bio"],
            )
            return redirect("home")


class EditProfileView(View):
    """can edit your profile"""

    def get(self, request, id):

        template = "generic_form.html"
        signed_in_member = request.user
        try:
            profile_user = MemberProfile.objects.get(member=signed_in_member)
            form = EditProfileForm(
                initial={
                    "first_name": profile_user.first_name,
                    "last_name": profile_user.last_name,
                    # "email": profile_user.email,
                    "profile_picture": profile_user.profile_picture,
                    "bio": profile_user.bio,
                }
            )
        except Exception as err:
            print(err)
            messages.add_message(
                request,
                message="You do not have a profile yet",
                level=messages.ERROR,
            )
            return redirect(reverse("profile", args=(id,)))
        context = {
            "signed_in_member": signed_in_member,
            "form": form,
            "profile_user": profile_user,
            "header": "Edit Profile",
        }
        return render(request, template, context)

    def post(self, request, id):

        target_member = Member.objects.get(id=id)
        profile_user = MemberProfile.objects.get(user=target_member)
        form = EditProfileForm(request.POST, request.FILES)
        try:
            if form.is_valid():
                data = form.cleaned_data
                profile_user.first_name = data["first_name"]
                profile_user.last_name = data["last_name"]
                profile_user.bio = data["bio"]
                profile_user.profile_picture = data["profile_picture"]
                profile_user.save()
                messages.add_message(
                    request,
                    message="You have sucessful target_member.profile_picturely edited your profile.",
                    level=messages.SUCCESS,
                )
                return redirect(reverse("profile", args=(id,)))
        except Exception as err:
            print(f"This is error:\n{err}")
            messages.add_message(
                request,
                message="There was an error editing your profile.",
                level=messages.ERROR,
            )
            return redirect(reverse("profile", args=(id,)))
