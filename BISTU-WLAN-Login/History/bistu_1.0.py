#!/usr/bin/env python
# -*- coding: utf-8 -*-
#version 1.0
import requests
import sys,getopt
from requests.packages import urllib3
urllib3.disable_warnings()
opts, args = getopt.getopt(sys.argv[1:], "hu:p:")
username=""
password=""
for op, value in opts:
    if op == "-u":
        username = value
    elif op == "-p":
        password = value

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
