from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
# Create your views here.

"""
class homePage(TemplateView):
	template_name = 'index.html'

class aboutPage(TemplateView):
	template_name = 'about-us.html'

class contactPage(TemplateView):
	template_name = 'contact.html'

class techPage(TemplateView):
	template_name = 'tech.html'
"""

def homePage(req):
	return render(req, 'index.html')

def aboutPage(req):
	return render(req, 'about-us.html')

def contactPage(req):
	return render(req, 'contact.html')

def techPage(req):
	return render(req, 'tech.html')