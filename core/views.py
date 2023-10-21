from django.shortcuts import render, redirect
from django.views import View
from django.core.mail import EmailMessage
from .models import Detail
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login



# Create your views here.

class MainView(View):

	def get(self, request):
		return render(request, 'core/index.html')

class SendMail(View):

	def get(self, request):
		return render(request, 'core/sendsingle.html')

	def post(self, request):
		subject = request.POST.get('subject')
		mail_body = request.POST.get('mail_body')
		email = EmailMessage(
		    subject,          # Email subject
		    mail_body,   # Email content
		    'amkelvinuche@gmail.com',   # Sender's email address
		    Detail.objects.values_list('email', flat=True),  # List of recipient email addresses
		    # reply_to=['another@example.com'],  # Optional reply-to email address
			)
		email.send()

		return redirect('/')
class SignIn(View):

	def get(self, request):
		return render(request, 'core/signin.html')

	def post(self, request):
		username = request.POST.get('username')
		password = request.POST.get('password')
		
		user = authenticate(username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('/')
		else:
			messages.info(request, 'account not found!')
		return redirect('/signin')

class SignUp(View):

    def get(self, request):
        return render(request, 'core/signup.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        password1 = request.POST.get('password1')
        user_name = User.objects.filter(username=username)

        if password != password1:
            messages.error(request, 'Passwords do not match.')
        elif user_name.exists():
            messages.error(request, 'Username is taken.')
        else:
            user = User.objects.create_user(username=username, password=password1)
            messages.success(request, 'Account created successfully.')
            return redirect('home')  # Use URL names or reverse() for redirects
        return redirect('signup')  # Use URL names or reverse() for redirects

