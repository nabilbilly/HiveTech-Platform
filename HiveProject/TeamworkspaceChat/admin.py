from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Message

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('user', 'content', 'timestamp')
    search_fields = ('user__username', 'content')
    list_filter = ('timestamp',)