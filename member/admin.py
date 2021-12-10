from django.contrib import admin

from member.models import Member, MemberProfile

# Register your models here.
admin.site.register(Member)
admin.site.register(MemberProfile)
