from django.template.loader import get_template
from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
	queryset = CoverImage.objects.all()
	queryset_client = Client.objects.all()
	context = {
    	"cover_list": queryset,
    	"client_list": queryset_client,
    }
	return render(request, "index.html",context)
