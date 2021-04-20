#shodan phish finder via favicon hash

import mmh3
import requests
import codecs
import base64
 
response = requests.get('hxxps://c.s-microsoft[.]com/favicon.ico')
favicon = codecs.encode(response.content,"base64")
hash = mmh3.hash(favicon)
print(hash)

#http.favicon.hash:-2057558656 -org:"Microsoft Corporation" -org:"Microsoft Azure" product:"Apache httpd" http.html:"Sign in"
