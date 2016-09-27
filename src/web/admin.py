from django.contrib import admin
from django.core.urlresolvers import reverse
from .models import *


# Register your models here.
class ProjectModelAdmin(admin.ModelAdmin):
	#list_editable = ["name"]
	list_filter = ["name"]
	list_display = ["__unicode__","name","order","featured"]
	list_editable = ["name","order","featured"]
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

class OurServicesModelAdmin(admin.ModelAdmin):
	list_display = ["__unicode__","name","text","featured"]
	list_editable = ["text"]

	class Meta:
		model = OurServices

class AboutUsModelAdmin(admin.ModelAdmin):
	list_display = ["__unicode__",]
	class Meta:
		model = AboutUs

class ClientImageModelAdmin(admin.ModelAdmin):
	#list_editable = ["title"]
	list_filter = ["name"]
	list_display = ["__unicode__","name","order"]
	list_editable = ["name","order"]
	search_fields = ["name"]
	class Meta:
		model = CoverImage

admin.site.register(AboutUs,AboutUsModelAdmin)
admin.site.register(OurServices,OurServicesModelAdmin)
admin.site.register(Project, ProjectModelAdmin)
admin.site.register(CoverImage,CoverImageModelAdmin)
admin.site.register(Client,ClientImageModelAdmin)
