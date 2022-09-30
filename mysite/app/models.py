from unittest.util import _MAX_LENGTH
import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

class Item(models.Model):
    category = models.CharField(max_length = 50)
    item_name = models.CharField(max_length = 50)
    description = models.CharField(max_length = 200)
    postdate = models.DateTimeField('posted on')

    def __str__(self):
        return self.item_obj
    
    def published(self):
        return self.postdate >= timezone.now() - datetime.timedelta(days=1)