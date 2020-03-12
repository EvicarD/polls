from django.contrib import admin
from .models import Book, Publisher, Author, Comment


class PublisherAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'address',
        'city',
        'state_province',
        'country',
        'website',
    )
    prepopulated_fields = {
        'slug': ('name',)
    }


admin.site.register(Book)
admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Author)
admin.site.register(Comment)
