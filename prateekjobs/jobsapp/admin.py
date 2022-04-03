from django.contrib import admin
from jobsapp.models import HydJobs,PuneJobs,BangloreJobs
# Register your models here.

class HydJobAdmin(admin.ModelAdmin):
    list_display = ['date','company','title','eligibiity','address','email','phone_number']
admin.site.register(HydJobs,HydJobAdmin)

class BangloreJobAdmin(admin.ModelAdmin):
    list_display = ['date','company','title','eligibiity','address','email','phone_number']
admin.site.register(BangloreJobs,BangloreJobAdmin)

class PuneJobAdmin(admin.ModelAdmin):
    list_display = ['date','company','title','eligibiity','address','email','phone_number']
admin.site.register(PuneJobs,PuneJobAdmin)
