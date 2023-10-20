# programs/admin.py

from django.contrib import admin
from .models import Program, ProgramCategory  # Import ProgramCategory

admin.site.register(Program)  # Register Program model
admin.site.register(ProgramCategory)  # Register ProgramCategory model
