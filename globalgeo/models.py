from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.


class CategoryBooks(models.Model):
    category_name = models.CharField(max_length=50)
    category_description = models.TextField()
    img = models.ImageField(upload_to='images/', blank=True)


    def __str__(self):
        return self.category_name


class Books(models.Model):
    books_name = models.CharField(max_length=50)
    books_description = models.TextField()
    books_img = models.ImageField(upload_to='images/', blank=True)
    category = models.ForeignKey(CategoryBooks, on_delete=models.CASCADE)
    book = models.FileField(upload_to='images/',null=True,blank=True)


    def __str__(self):
        return self.books_name


class CategoryPost(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=50)
    body = RichTextField()
    photo = models.ImageField(upload_to='images/', blank=True,null=True)
    author = models.CharField(max_length=20)
    date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(CategoryPost,on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post,related_name='comments',on_delete=models.CASCADE)
    body = models.TextField()
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

    def __str__(self):
        return self.name