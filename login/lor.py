import urllib2
import cookielib
from getpass import getpass
import sys
import os
from stat import *


def send_message(message,number):

	 
    	user_name = "8094047111"
    	passwd = "copenhagen1998"
        message = "+".join(message.split(' '))

 #logging into the sms site
    	url ='http://site24.way2sms.com/Login1.action?'
    	data = 'username='+user_name+'&password='+passwd+'&Submit=Sign+in'

 #For cookies

    	cj= cookielib.CookieJar()
    	opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))

 #Adding header details
    	opener.addheaders=[('User-Agent','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.120')]
    	try:
        	usock =opener.open(url, data)
    	except IOError:
        	print "error"
        #return()

    	jession_id =str(cj).split('~')[1].split(' ')[0]
    	send_sms_url = 'http://site24.way2sms.com/smstoss.action?'
    	send_sms_data = 'ssaction=ss&Token='+jession_id+'&mobile='+number+'&message='+message+'&msgLen=136'
    	opener.addheaders=[('Referer', 'http://site25.way2sms.com/sendSMS?Token='+jession_id)]
    	try:
        	sms_sent_page = opener.open(send_sms_url,send_sms_data)
    	except IOError:
        	print "error"
        #return()

    	print "success" 
    
