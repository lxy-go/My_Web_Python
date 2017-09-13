# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

class Book(object):
	def __init__(self,name):
		self.name = name

	def get_name(self):
		return self.name

def get_book_name():
	return "<<python base>>"

"""
def hello_books(request, bn):
#1	bn = None
#1	return render(request,'hello_books.html',{"books_name":bn}) 
#2	return render(request,'hello_books.html',{"books_nama":bn}) 
#3	传字典类型

	dict_e = {
		"1001":"<<python web指南>>",
		"1002":"<<python django指南>>",
		"1003":"<<python flask指南>>",
	}
	return render(request,'hello_books.html',{"books_name":dict_e})
#4 传模型对象
	b = Book("<<python base>>")
	return render(request,'hello_books.html',{"books_name":b})
#5 传成员方法
	b = Book("<<python base>>")
	return render(request,'hello_books.html',{"books_name":b.get_name})
#6 传函数
	return render(request,'hello_books.html',{"books_name":get_book_name})
"""

"""
def hello_books(request,bn):
#	return render(request,'hello_books.html',{"books_name":bn})
	bn1 = "python"
	bn2 = "php"
	return render(request,'hello_books.html',{"books_name1":bn1,"books_name2":bn2})

def hello_books(request,bn):
	l = ["python", "php","java"]
	return render(request,'hello_books.html',{"books_name":l})
"""	
def hello_books(request,bn):
	return render(request,'hello_books.html',{"books_name":bn})

def test(request):
	return HttpResponse("test page!!!")
