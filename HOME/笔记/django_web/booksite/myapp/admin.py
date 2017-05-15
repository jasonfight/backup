from django.contrib import admin
from myapp.models import *

# Register your models here.

admin.site.register(Publisher)
admin.site.register(Author,AuthorAdmin)
admin.site.register(Book,BookAdmin)
admin.site.register(User)

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','email')
    search_fields = ('first_name','last_name')

class BookAdmin(admin.ModelAdmin):
    list_display = ('title','publisher','publication_date')
    list_filter = ('publication_date',)
    data_hierarchy = 'publication_date'
    ording = ('-publication_date',)
    fields = ('title','author','publisher','publication_date')
