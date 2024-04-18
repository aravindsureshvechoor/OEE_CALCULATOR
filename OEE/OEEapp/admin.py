from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Machine)
admin.site.register(ProductionLog)
admin.site.register(Calculations)

