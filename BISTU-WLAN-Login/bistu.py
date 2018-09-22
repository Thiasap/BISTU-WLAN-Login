#!/usr/bin/env python
# -*- coding: utf-8 -*-
# version 1.1
import requests
import sys,getopt
from requests.packages import urllib3
import codecs,json
urllib3.disable_warnings()

opts, args = getopt.getopt(sys.argv[1:], "hu:p:c:s:")
username=""
password=""
for op, value in opts:
    if op == "-u":
        username = value
    elif op == "-p":
        password = value
    elif op == "-c":
    	dict=codecs.open(value)
    	conf = ''
    	for kms in dict:
    		conf = conf + kms
    	user_dict = eval(conf)
    	#print conf
    	params = json.loads(conf)
    	username = params['username']
    	password = params['password']
    elif op == "-s":
        save={  
                'username':username,
                'password':password
        }
        jsObj = json.dumps(save)  
        out = open(value,'w')  
        out.write(jsObj)  
        out.close() 
        print "Save Successful !" 


url="https://1.1.1.1/login.html"
slen=3120
post={	'buttonClicked':'4',
		'err_flag':'0',
		'err_msg':'',
		'info_flag':'0',
		'info_msg':'',
		'redirect_url':'',
		'network_name':'Guest+Network',
}
post['username']=username
post['password']=password

se=requests.post(url,data=post,verify=False)
if slen==len(se.text):
	print 'Login Successful !' 
else:
	print 'Login Failure'