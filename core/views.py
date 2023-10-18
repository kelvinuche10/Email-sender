from django.shortcuts import render, redirect
from django.views import View
from django.core.mail import EmailMessage
from .models import Detail



# Create your views here.

class MainView(View):

	def get(self, request):
		return render(request, 'core/index.html')

class SendSingle(View):

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
