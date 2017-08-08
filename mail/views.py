from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Mail
from .forms import MailForm
from django.contrib.auth.models import User
from pprint import pprint
# from django.contrib.auth.decorators import login_required
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

def signout(request):
	auth.logout(request)
	return redirect('login')

# this is function which will show them only those mails which they have to others 
def home(request):
	to_mail = Mail.objects.filter(user=User.objects.get(username=request.user.username))
	# import ipdb; ipdb.set_trace()
	return render(request, 'home.html', {'to_mail':  to_mail})

def inbox(request):
	list1 = []
	for data in  Mail.objects.filter(Receiver=User.objects.get(email=request.user.email).email):
		list1.append(data)
	# import ipdb; ipdb.set_trace()
	return render(request,"inbox.html",{'recieved_mail': list1})

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

def mail_remove(request,pk):
	mail = Mail.objects.get(pk=pk)
	mail.delete()
	return redirect('home')