from django.contrib import admin
from .models import CategoryBooks,Books,CategoryPost,Post,Comment


# Register your models here.

admin.site.register(CategoryBooks)
admin.site.register(Books)
admin.site.register(CategoryPost)
admin.site.register(Post)
admin.site.register(Comment)

