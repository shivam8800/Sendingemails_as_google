from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Mail
from .forms import MailForm
from django.contrib.auth.models import User
from pprint import pprint
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib import auth


def login(request):
	if request.method == 'POST':
		user = authenticate(request, username=request.POST.get('username'), password=request.POST.get('password'))
		if user:
			auth.login(request,user)
			return redirect('home')
		else:
			try:
			    user1 = User.objects.get(username=request.POST.get("username"))
			    messages.info(request, 'Please enter correct password.')
			    return redirect('login')
			except:
			    messages.info(request, 'Username and Password do not match.')
			    return redirect('login')

	else:
		return render(request, 'login.html', {})

@login_required
def signout(request):
	auth.logout(request)
	return redirect('login')

@login_required
# this is function which will show them only those mails which they have send to others means sending mails
def home(request):
	to_mail = Mail.objects.filter(user=User.objects.get(username=request.user.username),is_deleted_sender=True)
	# import ipdb; ipdb.set_trace()
	return render(request, 'home.html', {'to_mail':  to_mail})

@login_required
#from this we can see all the mail who have recived to login user
def inbox(request):
	list1 = Mail.objects.filter(Receiver=User.objects.get(email=request.user.email).email,is_deleted_receiver = False)
	# import ipdb; ipdb.set_trace()
	return render(request,"inbox.html",{'recieved_mail': list1})

@login_required
#for send email to other
def send_email(request):
	if request.method == 'POST':
		form = MailForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.user=User.objects.get(username=request.user.username)
			post.save()
			return redirect('home')
	else:	
		form = MailForm()
	return render(request, 'sent_mail.html', {'form': form})

@login_required
#for delete a mail
def mail_remove(request,pk,delete_id):
	mail = Mail.objects.get(pk=pk)
	if delete_id == '2':
		mail.is_deleted_receiver = True
		mail.save()
		return redirect('inbox')
	else:
		mail.is_deleted_sender = False
		mail.save()
		return redirect('home')