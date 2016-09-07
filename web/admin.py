from django.contrib import admin
from django.core.urlresolvers import reverse
from .models import *
# Register your models here.
class ProjectModelAdmin(admin.ModelAdmin):
	#list_editable = ["name"]
	list_filter = ["name"]
	list_display = ["__unicode__","name","image","order","text"]
	list_editable = ["name","image","order","text"]
	search_fields = ["name"]
	class Meta:
		model = Project

class CoverImageModelAdmin(admin.ModelAdmin):
	#list_editable = ["title"]
	list_filter = ["name"]
	list_display = ["__unicode__","name","image","order","text"]
	list_editable = ["name","image"]
	search_fields = ["name"]
	class Meta:
		model = CoverImage

admin.site.register(Project, ProjectModelAdmin)
admin.site.register(CoverImage,CoverImageModelAdmin)