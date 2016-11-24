#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
import json, time

from .models import User, TempLog

# Create your views here.

# 数据显示主页
def index(request):
	return HttpResponse(u'这是dataDisplay的主页！')

#手动输入数据页面
def input(request, userid):
	user = get_object_or_404(User, pk=userid)
	return render(request, 'dataDisplay/input.html', {'user':user})

#添加数据页面
def addData(request, userid, source):
	user = get_object_or_404(User, pk=userid)
	temp = float(request.POST['temp'])
	recv_time = timezone.now()
	recv_timestamp = int(time.mktime(recv_time.timetuple()))
	templog = TempLog(temperature=temp, recv_time=recv_time, recv_timestamp=recv_timestamp, user=user)
	templog.save()
	if source == 'web':
		return HttpResponseRedirect(reverse('dataDisplay:result',args=(user.id,)))
	else:
		return HttpResponse(u'get wifi data')
#显示数据结果的页面
def result(request, userid):
	user = get_object_or_404(User, pk=userid)
	latest_templog_list = user.templog_set.order_by('-recv_time')[:100]
	context = {'latest_templog_list':latest_templog_list}
	return render(request, 'dataDisplay/result.html', context)


