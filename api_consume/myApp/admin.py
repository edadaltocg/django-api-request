from django.contrib import admin
from myApp.models import Message

# Register your models here.
# When ceating a new db model, add it to the admin dashboard
admin.site.register(Message)


