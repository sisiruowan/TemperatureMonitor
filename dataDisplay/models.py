#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

'''
	数据表：
		1 User
		2 TempLog
'''

# Create your models here.

#用户类型
class User(models.Model):
	username = models.CharField(max_length = 30)
	password = models.CharField(max_length = 30)
	
#温度日志
class TempLog(models.Model):
	temperature = models.FloatField()
	recv_time = models.DateTimeField()
	recv_timestamp = models.IntegerField()
	user = models.ForeignKey(User, on_delete = models.CASCADE)


