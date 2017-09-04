from django.contrib import admin

# Register your models here.
from .models import Message, Conversation, ConversationUsers

admin.site.register(Message)
admin.site.register(ConversationUsers)
admin.site.register(Conversation)