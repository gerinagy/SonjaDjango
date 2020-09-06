from django.shortcuts import render
from django.core.mail import send_mail

def index(request):
	return render(request, 'index.html', {})

def contact(request):
	if request.method == "POST":
		message_name = request.POST['message_name']
		message_email = request.POST['message_email']
		message = request.POST['message']

		# send an email
		send_mail(
			message_name,	# subject
			message,	# message
			message_email,	# from email
			['nagy.gergi6@gmail.com']	# to email
			)

		return render(request, 'contact.html', {'message_name' : message_name})

	else:
		return render(request, 'contact.html', {})

def about(request):
	return render(request, 'about.html', {})

def blog(request):
	return render(request, 'blog.html', {})