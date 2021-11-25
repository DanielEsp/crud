from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator

MAIL_REGEX = RegexValidator(r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}$', 'Only valid email is accepted')
NAME_REGEX = RegexValidator(r'^[a-zA-Z]+(([\',. -][a-zA-Z ])?[a-zA-Z]*)*$', 'Only valid names accepted')
# Create your models here.
class User(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    date = models.DateTimeField(default=timezone.now, editable=False)
    name = models.CharField(max_length=100, validators=[NAME_REGEX])
    mail = models.CharField(max_length=100, validators=[MAIL_REGEX])