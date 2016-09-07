from django.template.loader import get_template
from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
	queryset = CoverImage.objects.all()

	context = {
    	"cover_list": queryset,
    }
	return render(request, "index.html",context)
