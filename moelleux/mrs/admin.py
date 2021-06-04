from django.contrib import admin
from .models import SearchModel, FeedbackModel

# Register your models here.
admin.site.register(SearchModel)
admin.site.register(FeedbackModel)
