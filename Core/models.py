from django.db import models


class Slider(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='slider-image/', null=True, blank=True)
    description = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'SliderTek'
        verbose_name_plural = 'SliderCut'


class Contact(models.Model):
    fullname = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    subject = models.CharField(max_length=50)
    message = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.fullname

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contact'
