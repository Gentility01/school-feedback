from django.contrib import admin
from .models import Feedback, Response, Vote
# Register your models here.
admin.site.register(Feedback)
admin.site.register(Response)
admin.site.register(Vote)