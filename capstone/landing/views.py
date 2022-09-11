from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
# Create your views here.

class homePage(TemplateView):
	template_name = 'index.html'

# def homePage(req):
	# return render(req, 'index.html')
	# return HttpResponse('Hello World!!')