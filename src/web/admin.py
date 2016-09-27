from django.contrib import admin
from django.core.urlresolvers import reverse
from .models import *


# Register your models here.
class ProjectModelAdmin(admin.ModelAdmin):
	#list_editable = ["name"]
	list_filter = ["name"]
	list_display = ["__unicode__","name","order","text","featured"]
	list_editable = ["name","order","text","featured"]
	search_fields = ["name"]
	class Meta:
		model = Project

class CoverImageModelAdmin(admin.ModelAdmin):
	#list_editable = ["title"]
	list_filter = ["name"]
	list_display = ["__unicode__","name","featured"]
	list_editable = ["name"	,"featured"]
	search_fields = ["name"]
	class Meta:
		model = CoverImage


class ClientImageModelAdmin(admin.ModelAdmin):
	#list_editable = ["title"]
	list_filter = ["name"]
	list_display = ["__unicode__","name","order"]
	list_editable = ["name","order"]
	search_fields = ["name"]
	class Meta:
		model = CoverImage

class CompanyAboutModelAdmin(admin.ModelAdmin):
	list_display = ["__unicode__","company_about","fb","tw"]
	class Meta:
		model= CompanyAbout

admin.site.register(Project, ProjectModelAdmin)
admin.site.register(CoverImage,CoverImageModelAdmin)
admin.site.register(Client,ClientImageModelAdmin)
admin.site.register(CompanyAbout,CompanyAboutModelAdmin)