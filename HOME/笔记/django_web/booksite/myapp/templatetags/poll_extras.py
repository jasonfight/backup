#!/usr/bin/python
#coding=utf-8

from django import template

register = template.Library()

@register.filter(name = 'cut')		#cut为自定义的过滤器名称
def cut(value,arg):
	return value.replace(arg,'##')	#自定义的操作
