
from django.contrib import admin
from django.contrib.admin import AdminSite
from django.contrib.auth.models import Group
from django.utils.translation import ugettext_lazy

from .models import *

admin.site.site_header = 'Megha Admin Panel'
admin.site.site_title = 'Megha Admin Panel'
admin.site.index_title = 'Change everything at here'

# class MyAdminSite(AdminSite):
#     # Text to put at the end of each page's <title>.
#     site_title = ugettext_lazy('gggggggggg')
#
#     # Text to put in each page's <h1> (and above login form).
#     site_header = ugettext_lazy('hhhhhhhhhhh')
#
#     # Text to put at the top of the admin index page.
#     index_title = ugettext_lazy('iiiiiiiiiiiii')
#
# admin_site = MyAdminSite()

# class MeghaAdmin(admin.ModelAdmin):
#     change_list_template = 'templates/megha_admin.html'

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



