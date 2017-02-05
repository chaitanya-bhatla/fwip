from django.conf.urls import patterns, include, url
from login.views import *
from django.contrib import admin
 
urlpatterns = patterns('',
    	
    #url(r'^$', 'django.contrib.auth.views.login'),
	url(r'^$',welcome_page),
	#url(r'^$',index),
	url(r'^logout/$', logout_page),
	url(r'^accounts/login/$', 'django.contrib.auth.views.login'), # If user is not login it will redirect to login page
	url(r'^register/$', index,name='register'),
	url(r'^register/ads/$',ads,name='ads'),
	url(r'^register/videoad/$',videoad),
#	url(r'^register/success/$', register_success),
#	url(r'^register/otp/$',otp_form,name='otp_form'),
	url(r'^register/success/$', register_success),	
	url(r'^index/$',index),	
	url(r'^home/$', home),
	url(r'^admin/', admin.site.urls),	
)
