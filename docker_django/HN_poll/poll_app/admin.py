from django.contrib import admin

# Register your models here.
from .models import Candidate
admin.site.register(Candidate)

from .models import Voter
admin.site.register(Voter)

