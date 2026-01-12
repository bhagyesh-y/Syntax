from django.contrib import admin
from .models import About

class AboutAdmin(admin.ModelAdmin):
    def had_add_permission(self,request):
        count = About.objects.all().count()
        if count == 0:
            return True
        else:
            return False
admin.site.register(About,AboutAdmin)
