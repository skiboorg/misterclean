from django.contrib import admin

from .models import *
class ServiceFeatureInline (admin.TabularInline):
    model = ServiceFeature
    extra = 0

class ServiceStepInline (admin.TabularInline):
    model = ServiceSteps
    extra = 0
class ServicePriceInline (admin.TabularInline):
    model = ServicePrice
    extra = 0


class ServiceImageInline(admin.TabularInline):
    model = ServiceImage
    readonly_fields = ('image_tag',)
    exclude = ('image_small',)
    extra = 0


class ServiceNameAdmin(admin.ModelAdmin):

    exclude = ['name_slug','name_lower']
    inlines = (ServiceFeatureInline, ServicePriceInline, ServiceImageInline, ServiceStepInline)
    class Meta:
        model = ServiceName

admin.site.register(ServiceName,ServiceNameAdmin)
admin.site.register(SeoTag)
# admin.site.register(ServicePrice)
# admin.site.register(ServiceFeature)