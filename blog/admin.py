from django.contrib import admin
from .models import Post
from .models import Animal

# Register your models here.
admin.site.register( Post )

admin.site.register( Animal )