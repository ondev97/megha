from django.contrib import admin
from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class IndexSectionOne(models.Model):
    title = models.TextField()
    description = RichTextField(blank=True)

    def __str__(self):
        return self.title

class IndexSectionTwo(models.Model):
    image = models.ImageField(upload_to='images')
    description = RichTextField(blank=True)

class MediumImage(models.Model):
    image = models.ImageField(upload_to='images')
    dec = RichTextField(blank=True)

class IndexSectionThree(models.Model):
    title = models.TextField()
    url = models.TextField()
    description = RichTextField(blank=True)

class IndexSectionFour(models.Model):
    title = models.TextField()

class Questions(models.Model):
    ques = models.TextField()
    ans = RichTextField(blank=True)

class OrderSection(models.Model):
    title = models.TextField()
    description = RichTextField(blank=True)

class OrderStep(models.Model):
    title = models.TextField()
    dec = RichTextField(blank=True)

class TestimonialsSectionOne(models.Model):
    title = models.TextField()
    description = RichTextField(blank=True)

class TestimonialsSectionTwo(models.Model):
    title = models.TextField()

class Video(models.Model):
    url = models.TextField()

class Testimonial(models.Model):
    content = RichTextField(blank=True)
    address = RichTextField(blank=True)
