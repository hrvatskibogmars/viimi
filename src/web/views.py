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
	
	try:
		queryset_projects = Project.objects.all().filter(featured=True)
	except ObjectDoesNotExist:
		queryset_projects = None
	

	try:
		queryset_ourservices = OurServices.objects.get(featured=True)
	except ObjectDoesNotExist:
		queryset_ourservices = None

	try:
		queryset_aboutus = AboutUs.objects.get(pk=1)
	except ObjectDoesNotExist:
		queryset_aboutus = None
	
	
	queryset_client = Client.objects.all()


	context = {
    	"cover": queryset_cover,
    	"client_list": queryset_client,
    	"project_list": queryset_projects,
    	"ourservice": queryset_ourservices,
    	"aboutus":queryset_aboutus,

    }
	return render(request, "index.html",context)
