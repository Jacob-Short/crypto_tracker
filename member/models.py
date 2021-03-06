from django.db import models
from django.utils import timezone
from django.contrib.auth.models import (
    AbstractUser,
)
from django.utils.translation import ugettext_lazy as _


class Member(AbstractUser):
    """a user account for site"""

    def __str__(self):
        return self.username


class MemberProfile(models.Model):
    """OTO with user for personal attributes"""

    member = models.OneToOneField(Member, on_delete=models.CASCADE)
    first_name = models.CharField(
        max_length=150,
        blank=True,
        null=True,
    )
    last_name = models.CharField(
        max_length=150,
        blank=True,
        null=True,
    )
    profile_picture = models.ImageField(
        upload_to="images/",
        max_length=100,
        default="images/default_profile_picture.jpeg",
    )
    bio = models.TextField(_("bio"), null=True, blank=True)
    is_new = models.BooleanField(
        _("new status"),
        default=True,
    )
    created_at = models.DateTimeField(default=timezone.now())

    def full_name(self):
        return f"{self.first_name} {self.last_name}"
