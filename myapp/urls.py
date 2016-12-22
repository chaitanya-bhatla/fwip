from django.conf.urls import patterns, include, url
from login.views import *
from django.contrib import admin
 
urlpatterns = patterns('',
    	
    #url(r'^$', 'django.contrib.auth.views.login'),
    url(r'^$',index),
    url(r'^logout/$', logout_page),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'), # If user is not login it will redirect to login page
    url(r'^register/$', register),
    url(r'^register/success/$', register_success),
    url(r'^register/otp/$',otp_form),
    url(r'^otp/success/$', otp_success),	
    url(r'^index/$',index),	
    url(r'^home/$', home),
    url(r'^admin/', admin.site.urls),	
)
