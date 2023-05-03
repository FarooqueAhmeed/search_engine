from django.contrib import admin
from search.models import *
# Register your models here.
admin.site.register(SearchResult)
admin.site.register(Blocked)
admin.site.register(Searches)