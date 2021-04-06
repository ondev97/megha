from django.contrib import admin
from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class IndexSectionOne(models.Model):
    title = models.CharField(max_length=250)
    description = RichTextField(blank=True)

    def __str__(self):
        return self.title

class IndexSectionTwo(models.Model):
    image = models.ImageField(upload_to='images')
    description = RichTextField(blank=True)

    def __str__(self):
        return self.description

class MediumImage(models.Model):
    image = models.ImageField(upload_to='images')
    dec = RichTextField(blank=True)

    def __str__(self):
        return self.dec

class IndexSectionThree(models.Model):
    title = models.CharField(max_length=250)
    url = models.TextField()
    description = RichTextField(blank=True)

    def __str__(self):
        return self.title

class IndexSectionFour(models.Model):
    title = models.CharField(max_length=250)

    def __str__(self):
        return self.title

class Questions(models.Model):
    ques = models.TextField()
    ans = RichTextField(blank=True)

    def __str__(self):
        return self.ques

class OrderSection(models.Model):
    title = models.CharField(max_length=250)
    description = RichTextField(blank=True)

    def __str__(self):
        return self.title

class OrderStep(models.Model):
    title = models.CharField(max_length=250)
    dec = RichTextField(blank=True)

    def __str__(self):
        return self.title

class TestimonialsSectionOne(models.Model):
    title = models.CharField(max_length=250)
    description = RichTextField(blank=True)

    def __str__(self):
        return self.title

class TestimonialsSectionTwo(models.Model):
    title = models.CharField(max_length=250)

    def __str__(self):
        return self.title

class Video(models.Model):
    url = models.TextField()

    def __str__(self):
        return self.url

class Testimonial(models.Model):
    content = RichTextField(blank=True)
    address = RichTextField(blank=True)

    def __str__(self):
        return self.address
