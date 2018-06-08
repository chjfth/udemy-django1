from django.contrib import admin

# Register your models here.

from first_app.models import Topic,Webpage,AccessRecord

class WebpageAdmin(admin.ModelAdmin):
	list_display = ['topic', 'name', 'url']

admin.site.register(Topic)
admin.site.register(Webpage, WebpageAdmin)
admin.site.register(AccessRecord)
