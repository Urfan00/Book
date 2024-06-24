from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Genre'
        verbose_name_plural = 'Genres'


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    birthday = models.DateField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.first_name} - {self.last_name}'


class Book(models.Model):
    title = models.CharField(max_length=150)

    image = models.ImageField(upload_to='media/book-image', null=True, blank=True)

    price = models.PositiveIntegerField()
    in_sale = models.BooleanField(default=False)
    percent = models.PositiveIntegerField(null=True, blank=True)
    new_price = models.PositiveIntegerField(null=True, blank=True)

    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    genre = models.ManyToManyField(Genre)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):

        if self.in_sale and 0 < self.percent <= 100:
            self.new_price = self.price - self.price * self.percent / 100

        super().save(*args, **kwargs)

