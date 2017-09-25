from messaging.models import Message, Conversation, ConversationUsers

def add_variable_to_context(request):
	unreadMessages = 0
	if request.user.is_authenticated():
		unreadMessages = Message.objects.filter(recipient = request.user).filter(read = False).count()
		print("checked for messages, found"+str(unreadMessages))
	return {'unreadMessages': unreadMessages}
