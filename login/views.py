from django.shortcuts import render

# Create your views here.
#views.py
from login.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from login.models import Post, Access
from login.lor import *
from uuid import getnode as get_mac
from subprocess import Popen, PIPE
import os
from random import randint

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def get_server_mac():
	mac=get_mac()
	return hex(mac)

def get_mac(IP):
	pid = Popen(["arp", "-n", IP], stdout=PIPE)
	s = pid.communicate()[0]
	if re.search(r"(([a-f\d]{1,2}\:){5}[a-f\d]{1,2})", s) is None:
		return 'localhost'
	mac = re.search(r"(([a-f\d]{1,2}\:){5}[a-f\d]{1,2})", s).groups()[0]
	return mac

def ads(request):
	return render_to_response('otp/ad.html')
	

def index(request):
	ip= get_client_ip(request)
    	mac= get_mac(ip)	
    
	if request.method == 'POST':
        	form = AccessForm(request.POST)
		if form.is_valid():
			name=form.cleaned_data['name']
			phone=form.cleaned_data['phone']
			OTP=randint(100, 999)
			obj=Access(name=name,ip=ip,mac=mac,phone=phone,OTP=OTP)
			
			send_message('Your OTP is '+str(OTP),phone)
			obj.save()
       		##return HttpResponseRedirect('/register/otp/')
		return HttpResponseRedirect('/register/ads/')
	else:
        	form = AccessForm()
    		variables = RequestContext(request, {'form': form})
	
	return render_to_response('user.html',variables,)


@csrf_protect
def register(request):
    print '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
	
	if form.is_valid():
            user = User.objects.create_user(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password1'],
            email=form.cleaned_data['email']
            )
		
	    newPost=Post(author=user,title=form.cleaned_data['option'])
	    newPost.save()		    	
	    print '######################################################################'
	    print form.cleaned_data['option']      
        			
            return HttpResponseRedirect('/register/success/')
    else:
        form = RegistrationForm()
    variables = RequestContext(request, {
    'form': form
    })
 
    return render_to_response(
    'registration/register.html',
    variables,
    )
 
def otp_form(request):
	if request.method == 'POST':
		form = OtpForm(request.POST)
		
	
		if form.is_valid():
			print '^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^'
			print form.cleaned_data['otp']

			ip=get_client_ip(request)
			mac=get_mac(ip)
				
			
			obj=Access.objects.filter(mac=mac)
			if obj is None:
				print 'Not registered'
				return HttpResponseRedirect('/')
			else:
				print '*************************************************************'
				for i in obj:
					print i.OTP
				otp=obj[len(obj)-1].OTP
				otp=str(otp)
				print '%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%'
				print otp
				if otp==str(form.cleaned_data['otp']):
					print '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'
					print mac
					command="echo 'copenhagen1996' | sudo -S iptables -t mangle -I internet 1 -m mac --mac-source "+mac+" -j RETURN"
					os.system(command)
					return HttpResponseRedirect('/otp/success/')
					
				else:
					return HttpResponseRedirect('/register/otp/')		
			
	else:
        	form = OtpForm()
    		variables = RequestContext(request, {'form': form    })
 
    		return render_to_response('otp/form.html', variables,    )	

def register_success(request):
    return render_to_response(
    'registration/success.html',
    )
def otp_success(request):
    return render_to_response(
    'otp/success.html',
    )

def otp(request):
	return render_to_response('otp/form.html',)

def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')
 
@login_required
def home(request): 
   
    return render_to_response(
    'home.html',
    { 'user': request.user }
    )
