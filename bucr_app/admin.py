from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Restaurant)
admin.site.register(Table)
admin.site.register(Reservation)
admin.site.register(UserProfile)
admin.site.register(Review)
admin.site.register(Waitlist)
admin.site.register(Toilet)
