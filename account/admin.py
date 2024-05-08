from django.contrib import admin
from .models import Subscriber, User, OneTimePassword

admin.site.register(User)
admin.site.register(OneTimePassword)
admin.site.register(Subscriber)