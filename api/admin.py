from django.contrib import admin
from .models import Intent, Phrase, User

admin.site.register(Intent)
admin.site.register(Phrase)
admin.site.register(User)