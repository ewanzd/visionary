from django.contrib import admin
from .models import Person, Notebook, Note

# Register your models here.
admin.site.register(Person)
admin.site.register(Notebook)
admin.site.register(Note)
