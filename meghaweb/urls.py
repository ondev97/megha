from  django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('testimonials', views.testimonials, name='testimonials'),
    path('contact-us', views.contactus, name='contactus'),
    path('make_order', views.make_order, name='make_order'),
    path('make_question', views.make_question, name='make_question'),
]