from django.contrib import admin
from .models import Question, Answer, Musician, Album
# Register your models here.
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Musician)
admin.site.register(Album)