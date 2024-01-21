from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


# Create your models here.
class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Image_Journal(models.Model):
    Image = models.ImageField(upload_to="uploads/")



class Journal(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    content = RichTextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publication_date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    thumbnail = models.ImageField(upload_to="uploads/")
    comments_allowed = models.BooleanField(default=True)

    def __str__(self):
        return self.title
