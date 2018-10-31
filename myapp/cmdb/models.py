# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class user(models.Model):
    name = models.CharField(max_length=128, unique=True)
    password = models.CharField(max_length=256)
