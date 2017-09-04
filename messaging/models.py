from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Conversation(models.Model):
	title = models.CharField(max_length =250)

	def __str__(self):
		return self.title

class Message(models.Model):
	sent = models.DateTimeField(auto_now_add=True)
	read= models.BooleanField(default=False)
	text = models.TextField()	
	sender = models.ForeignKey(User, related_name="sender")
	recipient = models.ForeignKey(User, related_name="recipient")
	conversation = models.ForeignKey(Conversation, related_name="messageConversation")

	def __str__(self):
		return self.sender.first_name + ' '+ self.sender.last_name + ': '+ self.text

class ConversationUsers(models.Model):
	user = 	models.ForeignKey(User, related_name="user")
	conversation = models.ForeignKey(Conversation, related_name="usersConversation")




