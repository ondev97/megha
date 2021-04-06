from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.

class IndexSectionOne(models.Model):
    class Meta:
        verbose_name_plural = 'Index Section One'

    title = models.CharField(max_length=250)
    description = RichTextField(blank=True)

    def __str__(self):
        return self.title


class IndexSectionTwo(models.Model):
    class Meta:
        verbose_name_plural = 'Index Section Two'

    image = models.ImageField(upload_to='images')
    description = RichTextField(blank=True)

    def __str__(self):
        return self.description


class MediumImage(models.Model):
    class Meta:
        verbose_name_plural = 'Medium Images'

    image = models.ImageField(upload_to='images')
    dec = RichTextField(blank=True)

    def __str__(self):
        return self.dec


class IndexSectionThree(models.Model):
    class Meta:
        verbose_name_plural = 'Index Section Three'

    title = models.CharField(max_length=250)
    url = models.TextField()
    description = RichTextField(blank=True)

    def __str__(self):
        return self.title


class IndexSectionFour(models.Model):
    class Meta:
        verbose_name_plural = 'Index Section Four'

    title = models.CharField(max_length=250)

    def __str__(self):
        return self.title


class Questions(models.Model):
    class Meta:
        verbose_name_plural = 'Questions'

    ques = models.TextField()
    ans = RichTextField(blank=True)

    def __str__(self):
        return self.ques


class OrderSection(models.Model):
    class Meta:
        verbose_name_plural = 'Order Section'

    title = models.CharField(max_length=250)
    description = RichTextField(blank=True)

    def __str__(self):
        return self.title


class OrderStep(models.Model):
    class Meta:
        verbose_name_plural = 'Order Steps'

    title = models.CharField(max_length=250)
    dec = RichTextField(blank=True)

    def __str__(self):
        return self.title


class TestimonialsSectionOne(models.Model):
    class Meta:
        verbose_name_plural = 'Testimonials Section One'

    title = models.CharField(max_length=250)
    description = RichTextField(blank=True)

    def __str__(self):
        return self.title


class TestimonialsSectionTwo(models.Model):
    class Meta:
        verbose_name_plural = 'Testimonials Section Two'

    title = models.CharField(max_length=250)

    def __str__(self):
        return self.title


class Video(models.Model):
    class Meta:
        verbose_name_plural = 'Videos'

    url = models.TextField()

    def __str__(self):
        return self.url


class Testimonial(models.Model):
    class Meta:
        verbose_name_plural = 'Testimonials'

    content = RichTextField(blank=True)
    address = RichTextField(blank=True)

    def __str__(self):
        return self.address
