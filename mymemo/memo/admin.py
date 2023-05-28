from django.contrib import admin
from .models import Memo

@admin.register(Memo)
class MemoModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'writer', 'description', 'created', 'edited')
    list_filter = ('created','edited' )