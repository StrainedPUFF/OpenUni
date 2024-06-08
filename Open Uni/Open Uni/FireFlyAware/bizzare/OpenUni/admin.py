# from django.contrib import admin
# # from .models import Question, Answer, Musician, Album
# from .models import Category, Provider

# # Register your models here.
# # admin.site.register(Question)
# # admin.site.register(Answer)
# # admin.site.register(Musician)
# # admin.site.register(Album)
# class CategoryAdmin(admin.ModelAdmin):
#     fieldsets = [
#         (None, {"fields": ["category_text"]}),
#         ("Date information", {"fields": ["pub_date"]}),
#     ]


from django.contrib import admin

from .models import Category, Provider


class ProviderInline(admin.StackedInline):
    model = Provider
    extra = 3


class CategoryAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["category_text"]}),
        ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]
    inlines = [ProviderInline]
    list_display = [ "pub_date",]
    list_filter = ["pub_date"]
    
admin.site.register(Category, CategoryAdmin)
admin.site.register(Provider)

