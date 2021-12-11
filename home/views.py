from django.shortcuts import redirect, render, reverse
from django.views.generic import View, CreateView

# models
from member.models import Member, MemberProfile

# message count
from messaging.views import get_messages_count, get_notifications_count


from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages


class IndexView(View):
    """index page upon coming to site"""

    def get(self, request):

        signed_in_member = request.user
        template = "index.html"
        context = {"signed_in_member": signed_in_member}
        return render(request, template, context)

    def post(self, request):
        ...


class HomeView(View, LoginRequiredMixin):
    """index page upon coming to site"""

    def get(self, request):

        signed_in_member = request.user
        message_count = get_messages_count(signed_in_member)
        notification_count = get_notifications_count(signed_in_member)
        template = "home.html"
        context = {
            "signed_in_member": signed_in_member,
            "message_count": message_count,
            "notification_count": notification_count,
        }
        return render(request, template, context)

    def post(self, request):
        ...


def about(request):
    template = "about.html"
    signed_in_member = request.user
    message_count = get_messages_count(signed_in_member)
    notification_count = get_messages_count(signed_in_member)

    context = {
        "signed_in_member": signed_in_member,
        "message_count": message_count,
        "notification_count": notification_count,
    }
    return render(request, template, context)
