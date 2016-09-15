from django.contrib import admin

from . import models


class EntryAdmin(admin.ModelAdmin):
    # Note: Admin created entries do not require modified or comments_count fields
    list_display = ('title', 'published_date', 'created_date')
    readonly_fields = ('comment_count', 'modified_date')



admin.site.register(models.Entry, EntryAdmin)
