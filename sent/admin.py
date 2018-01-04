from django.contrib import admin
from sent.models import Posting


class PostingAdmin(admin.ModelAdmin):
    list_display = ('id','message','created_at')

# Register your models here.
admin.site.register(Posting)
