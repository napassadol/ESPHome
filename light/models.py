# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import datetime

# Create your models here.
class light(models.Model):
    intensity = models.IntegerField(default=0)
    date = models.DateTimeField(default=datetime.now, blank=True)