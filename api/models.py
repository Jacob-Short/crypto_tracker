from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

# models
from member.models import Member


class FavoriteCrypto(models.Model):
    """users can save a crypto into their watch list"""

    user = models.ForeignKey(Member, on_delete=models.CASCADE)
    symbol = models.CharField(
        max_length=150,
        blank=True,
        null=True,
    )
    name = models.CharField(
        max_length=150,
        blank=True,
        null=True,
    )
    rank = models.IntegerField()
    price = models.IntegerField()  # will need to make the price pull frequently
    date_added = models.DateTimeField()
    date_added_as_fav = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.symbol
