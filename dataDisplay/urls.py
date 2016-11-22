#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-11-21 15:00:04
# @Author  : Alex Tang (1174779123@qq.com)
# @Link    : http://t1174779123.iteye.com
'''
	description:
'''

from django.conf.urls import url 
from . import views

app_name = 'dataDisplay'
urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^(?P<userid>[0-9]+)/addData/(?P<source>[a-z]+)/$', views.addData, name='addData'),
	url(r'^(?P<userid>[0-9]+)/input/$', views.input, name='input'),
	url(r'^(?P<userid>[0-9]+)/result/$', views.result, name='result'),
]
