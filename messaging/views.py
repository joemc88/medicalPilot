from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from django.contrib.auth.views import logout
from django.contrib.auth import authenticate, login
from userAdmin.models import Patient, Doctor, Administrator
from django.contrib.auth.models import User
from .models import Message, Conversation, ConversationUsers
from django.db.models import Q
from gcm import *
def index(request):
	try:
		convosUsersIn = ConversationUsers.objects.filter(user = request.user)
		convos = []
		for i in convosUsersIn:
			convos.append(i.conversation.id)
		conversations = Conversation.objects.filter(id__in = convos)
	except ConversationUsers.DoesNotExist:
		conversations = {}
	context = {
		'conversations' : conversations
	}
	return render(request, 'messaging/index.html', context)



def messageForm(request):
	doctors = Doctor.objects.all()
	admins = Administrator.objects.all()
	patients = Patient.objects.filter(primary_physician = request.user.id)
	context = {
		'admins': admins,
		'doctors' : doctors ,
		'patients' : patients
	}
	return render(request, 'messaging/messageForm.html', context)

def sendMessage(request):

	conversation = 0
	try:
		x =  Message.objects.filter(sender = request.user, recipient =User.objects.get(id = request.POST.get('recipient','')) ).first()
		if x != None:
				conversation =x.conversation
		else:
			raise Message.DoesNotExist
	

	except Message.DoesNotExist: 	
		try:	
			x = Message.objects.filter(sender = User.objects.get(id = request.POST.get('recipient','')), recipient = request.user).first()
			if x != None:
				conversation = x.conversation
			else:
				raise Message.DoesNotExist
		except Message.DoesNotExist:
			print("LOG: no message found ")
			


	print("LOG: conversation status: "+str(conversation))

	if conversation == 0:
		print("no existing conversation found creating a new one")
		conversation = Conversation.objects.create(
			#change to a better descriptor of the conversation
			title = User.objects.get(id =  request.user.id).first_name +"-"+ User.objects.get(id = request.POST.get('recipient','')).first_name
		)
		conversation.save()

		firstConversationUser = ConversationUsers.objects.create(conversation = conversation, user =  request.user )
		secondConversationUser = ConversationUsers.objects.create(conversation = conversation, user = User.objects.get(id =  request.POST.get('recipient','')))
		firstConversationUser.save()
		secondConversationUser.save()

	message = Message.objects.create(
		text = request.POST.get('message',''),
		sender =request.user,
		recipient = User.objects.get(id = request.POST.get('recipient','')),
		conversation = conversation
	)
	message.save()
	print('attempting to send notification to')
	token = Patient.objects.get(user = User.objects.get(id = request.POST.get('recipient',''))).deviceToken
	print(token)
	gcm = GCM("AAAA3EPwcVU:APA91bGQKwkhEKjWQf5CPAbVXXzhFTa5tpl6IJ2VYSAb5mbn2dBF5ppMUAKzm8OAKR4NRkX3x-Juyk9TBcqjKUmLxUWAXU33j_9KHCsyyIzaJ4up_2dhFxt1wkw9OthRXrXFob11QGPl")
	data = {'message': 'You have recieved a new message'}
	gcm.plaintext_request(registration_id=token, data = data) 

	return redirect('/messaging')


def sendReply(request):

	conversation = Conversation.objects.get(id  =request.POST.get('conversation_id',''))
	messages = Message.objects.filter(conversation = conversation)

	context = {'messages': messages, 'conversation': conversation}

	message = Message.objects.create(
		text = request.POST.get('message',''),
		sender =request.user,
		recipient = User.objects.get(id = request.POST.get('recipient','')),
		conversation = conversation,
		read = False
	)
	message.save()
	print('attempting to send notification to')
	token = Patient.objects.get(user = User.objects.get(id = request.POST.get('recipient',''))).deviceToken
	print(token)
	gcm = GCM("AAAA3EPwcVU:APA91bGQKwkhEKjWQf5CPAbVXXzhFTa5tpl6IJ2VYSAb5mbn2dBF5ppMUAKzm8OAKR4NRkX3x-Juyk9TBcqjKUmLxUWAXU33j_9KHCsyyIzaJ4up_2dhFxt1wkw9OthRXrXFob11QGPl")
	data = {'message': 'You have recieved a new message'}
	gcm.plaintext_request(registration_id=token, data = data) 

	return redirect('/messaging/conversation/'+str(conversation.id))


def conversation(request, conversation_id):

	conversation = Conversation.objects.get(id  =conversation_id)
	messages = Message.objects.filter(conversation = conversation)
	for message in messages:
		if message.sender != request.user:
			message.read = True
			message.save()
	#get implicit recipient from previous messages
	try:
		recipient = Message.objects.filter(conversation = conversation).filter(sender = request.user).first().recipient
	except :
		recipient =  Message.objects.filter(conversation = conversation).filter(recipient = request.user).first().sender

	context = {
		'messages': messages,
		'conversation': conversation,
		'recipient': recipient
	}

	return render(request, 'messaging/conversation.html', context)