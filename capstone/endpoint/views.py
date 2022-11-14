from django.shortcuts import render

# Create your views here.
def apiPage(req):
    return render(req, "api.html")
