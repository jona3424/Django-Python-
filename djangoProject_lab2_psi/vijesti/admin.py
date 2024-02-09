from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(Vijest)
admin.site.register(Komentar)
admin.site.register(Korisnik)
