from django.db import models
from Account.models import Account
from Story.models import Category, Tag


class Recipes(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='Recipe')
    content = models.TextField()
    show_date = models.DateField()

    tag = models.ManyToManyField(Tag)
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Recipe'
        verbose_name_plural = 'Recipes'
