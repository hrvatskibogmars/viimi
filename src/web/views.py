from django.template.loader import get_template
from django.shortcuts import render
from .models import *
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.
def index(request):
	#queryset_cover = CoverImage.objects.get(id=1)
	try:
		queryset_cover = CoverImage.objects.get(featured=True)
	except ObjectDoesNotExist:
		queryset_cover = None
	
	queryset_client = Client.objects.all()
	queryset_projects = Project.objects.all()



	context = {
    	"cover": queryset_cover,
    	"client_list": queryset_client,
    	"project_list": queryset_projects,
    }
	return render(request, "index.html",context)
