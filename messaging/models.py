from django.db import models
from django.utils import timezone
from member.models import Member


class Message(models.Model):

    body = models.TextField(max_length=500)
    author = models.ForeignKey(
        Member, related_name="%(class)s_author", null=True, on_delete=models.CASCADE
    )
    recipient = models.ForeignKey(
        Member, related_name="%(class)s_recipient", null=True, on_delete=models.CASCADE
    )
    is_new = models.BooleanField(default=True)
    time_sent = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.body


class MessageNotification(models.Model):

    message = models.ForeignKey(
        Message, related_name="%(class)s_message", null=True, on_delete=models.CASCADE
    )
    member_notified = models.ForeignKey(
        Member,
        related_name="%(class)s_member_notified",
        null=True,
        on_delete=models.CASCADE,
    )

    is_new = models.BooleanField(default=True)
    time_notified = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.message.body

    def notification_from(self):
        return self.message.author
