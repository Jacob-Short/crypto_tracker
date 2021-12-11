from django.contrib.auth.models import User
from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib import messages
from django.views.generic import View
from django.db.models import Q

# models
from messaging.models import Message, MessageNotification
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
                body=data["body"], author=request.user, recipient=recipient
            )
            create_message_notification(new_message, recipient)
            messages.add_message(
                request, message="Message sent", level=messages.SUCCESS
            )
            return HttpResponseRedirect(reverse("profile", args=(request.user.id,)))


def member_messages(request, id):
    """members can view all of their messages
    from other members
    """
    template = "messaging.html"
    target_member = Member.objects.get(id=request.user.id)
    signed_in_member = Member.objects.get(id=id)

    message_count = get_messages_count(signed_in_member)
    notification_count = get_notifications_count(signed_in_member)

    member_messages = Message.objects.filter(recipient=signed_in_member)
    context = {
        "member_messages": member_messages,
        "signed_in_member": signed_in_member,
        "target_member": target_member,
        "message_count": message_count,
        "notification_count": notification_count,
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


def create_message_notification(message, tagged):
    all_members = Member.objects.all()
    names = [x.username for x in all_members]
    print(names)
    member_string = ""
    member_string += str(tagged)
    print(member_string)
    target_member = Member.objects.get(username=member_string)
    notification = MessageNotification.objects.create(
        message=message,
        member_notified=target_member,
    )


def member_notifications(request, id):
    """members can view all of their notifications"""

    template = "notifications.html"
    signed_in_member = Member.objects.get(id=id)

    message_count = get_messages_count(signed_in_member)
    notification_count = get_notifications_count(signed_in_member)

    new_member_notifications = MessageNotification.objects.filter(
        Q(member_notified=signed_in_member) & Q(is_new=True)
    )
    old_member_notifications = MessageNotification.objects.filter(
        Q(member_notified=signed_in_member) & Q(is_new=False)
    )

    context = {
        "old_member_notifications": old_member_notifications,
        "new_member_notifications": new_member_notifications,
        "signed_in_member": signed_in_member,
        "message_count": message_count,
        "notification_count": notification_count,
    }
    for notification in new_member_notifications:
        notify_seen(notification)
    return render(request, template, context)


def get_notifications_count(logged_in_member):
    """return count of active message"""
    signed_in_member = logged_in_member
    new_member_notifications = MessageNotification.objects.filter(
        Q(member_notified=signed_in_member) & Q(is_new=True)
    )

    return len(new_member_notifications)


def notify_seen(notification):
    notification.is_new = False
    notification.save()
