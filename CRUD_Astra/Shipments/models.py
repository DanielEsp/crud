from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

# Create your models here.
class Shipment(models.Model):

    class Status(models.TextChoices):
        DRAFT = 'DF', _('Draft')
        PENDING = 'PD', _('Pending')
        DELIVERED = 'DV', _('Delivered')

    id = models.AutoField(primary_key=True, editable=False)
    date = models.DateTimeField(default=timezone.now, editable=False)
    owner = models.CharField(max_length=100)
    status = models.CharField(
        max_length=2,
        choices=Status.choices,
        default=Status.DRAFT)
