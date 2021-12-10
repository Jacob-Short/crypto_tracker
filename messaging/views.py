from django.contrib.auth.models import User
from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib import messages
from django.views.generic import View

# models
from messaging.models import Message
from member.models import Member

# forms
from messaging.forms import SendMessageForm


class SendMessageView(View):
    """member can send another member a direct message"""

    def get(self, request, id):

        template = "generic_form.html"
        signed_in_member = request.user

        form = SendMessageForm()

        context = {
            "form": form,
            "header": "Send Message",
            "signed_in_member": signed_in_member,
        }
        return render(request, template, context)

    def post(self, request, id):
        form = SendMessageForm(request.POST)
        recipient = Member.objects.get(id=id)

        if form.is_valid():
            data = form.cleaned_data
            new_message = Message.objects.create(
                message=data["message"], author=request.user, recipient=recipient
            )
            messages.add_message(
                request, message="Message sent", level=messages.SUCCESS
            )
            return HttpResponseRedirect(reverse("member-view", args=(request.id,)))


def member_messages(request, id):
    """members can view all of their messages
    from other members
    """
    template = "messaging.html"
    target_member = Member.objects.get(id=request.user.id)
    signed_in_member = Member.objects.get(id=id)

    member_messages = Message.objects.filter(recipient=signed_in_member)
    message_count = get_messages_count(signed_in_member)
    context = {
        "member_messages": member_messages,
        "signed_in_member": signed_in_member,
        "target_member": target_member,
        "message_count": message_count
    }
    return render(request, template, context)


def delete_message(request, id):
    del_message = Message.objects.get(id=id)
    user_id = request.user.id
    del_message.delete()
    messages.add_message(request, message="Message deleted", level=messages.ERROR)
    return HttpResponseRedirect(reverse("my-messages", args=(user_id,)))


def get_messages_count(logged_in_member):
    """return count of active message"""
    signed_in_member = logged_in_member
    member_messages = Message.objects.filter(recipient=signed_in_member)

    messages_count = len(member_messages)
    return messages_count
