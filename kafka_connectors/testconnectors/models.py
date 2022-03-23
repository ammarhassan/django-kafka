from django.db import models

# Create your models here.
from django.db.models import Model
from django.db.models import CharField, TextField


class KafkaMessages(Model):
    key = CharField(help_text='Key', max_length=255, blank=True, null=True)
    text = TextField(help_text='Text')
