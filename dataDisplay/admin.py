#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import TempLog, User
# Register your models here.

admin.site.register(TempLog)
admin.site.register(User)
