from django.contrib import admin

# models
from messaging.models import Message, MessageNotification

# Register your models here.
admin.site.register(Message)
admin.site.register(MessageNotification)
