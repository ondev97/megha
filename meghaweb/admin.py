from django.contrib import admin

from .models import *

admin.site.site_header = 'Megha Admin Panel'
admin.site.site_title = 'Megha Admin Panel'
admin.site.index_title = 'Change everything at here'


class StateAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


# Register your models here.

admin.site.register(IndexSectionOne)
admin.site.register(IndexSectionTwo)
admin.site.register(MediumImage)
admin.site.register(IndexSectionThree)
admin.site.register(IndexSectionFour)
admin.site.register(Questions)
admin.site.register(OrderSection)
admin.site.register(OrderStep)
admin.site.register(TestimonialsSectionOne)
admin.site.register(TestimonialsSectionTwo)
admin.site.register(Video)
admin.site.register(Testimonial)
