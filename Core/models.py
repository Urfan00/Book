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
