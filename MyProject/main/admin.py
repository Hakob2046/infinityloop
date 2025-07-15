from django.contrib import admin
from .models import *

admin.site.register(HeaderTitle)
admin.site.register(WhatWeDo)
admin.site.register(Features)
admin.site.register(Gallery)
admin.site.register(ContactUs)
admin.site.register(Testimonials)
admin.site.register(CountactUsWithPhone)


@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    list_display=('name','text')
    list_display_links=('name','text')
    search_fields=('name',)