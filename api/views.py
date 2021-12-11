from django.shortcuts import redirect, render, reverse
from django.views.generic import View, CreateView
from .helpers import CryptoCurrency

# models
from member.models import Member, MemberProfile

# message count
from messaging.views import get_messages_count


from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages


class Dashboard(View):
    """private view for users to look up cryptos
    and be able to save them and track their gains
    and losses
    """

    def get(self, request):
        template = "api_dashboard.html"
        signed_in_member = request.user
        message_count = get_messages_count(signed_in_member)

        cryptos = CryptoCurrency().get_all_coins()

        c = cryptos[0]
        print(c)

        context = {
            "signed_in_member": signed_in_member,
            "cryptos": cryptos,
            "message_count": message_count,
        }
        return render(request, template, context)

    def post(self, request):
        pass


class SearchCrypto(View):
    """search and view cryptos"""

    def get(self, request):
        pass

    def post(self, request):
        pass
