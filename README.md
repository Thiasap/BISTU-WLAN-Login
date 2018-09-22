#BISTU-WLAN-Login
Login WLAN "BISTU" by python

get bistu.py in:
https://github.com/Thiasap/BISTU-WLAN-Login/tree/master/BISTU-WLAN-Login

#Run in terminal: 
` python bistu.py -u username -p password `
You can use ` -s FILE ` to same login info in FILE, like:
` python bistu.py -u 2016019999 -p 123456 -s login.json `
And use ` python -c login.json ` login next time. 

#Run with a json:
make a new conf.json:
```xml
{
"username":"your username",
"password":"your password"
}
```
And then run: 
` python bistu.py -c conf.json `
