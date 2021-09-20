import json
import requests
import sys
#import urllib2
import urllib.request as urllib2


# Define the remote file to retrieve


AUTH_URL = 'http://localhost:8069/api/get/crm_data/'

headers = {'Content-type': 'application/json'}
# Remember to configure default db on odoo configuration file(dbfilter = ^db_name$)
# Authentication credentials

data = {
    'params': {
         'username': 'sgeede',
         'token': 'j43kFzt52SKEQ5cXDtPPpRhQXnwm24',
         'db': '14_AW_'
    }
}
params = {'username':'sgeede','token':'j43kFzt52SKEQ5cXDtPPpRhQXnwm24','db':'14_AW'}
res = requests.get(
    AUTH_URL, 
    params=params
)
#filedata = urllib2.urlopen('http://localhost:8069/web/content/ir.attachment/366/datas/sesudah.png')
#datatowrite = filedata.read()
 
#with open('Documents/AWODESTEST.jpeg', 'wb') as f:
#    f.write(datatowrite)

url = 'http://localhost:8069/web/content/ir.attachment/574/datas/AWODESTEST.jpeg'
r = requests.get(url, allow_redirects=True)

open('AWODESTEST.jpeg', 'wb').write(r.content)

print ('test',res)
#print (res.json()['list_data'])
#print (res.json()['list_data'][0]['passport_name'][0])


#import urllib2

def download_web_image(url):
    request = urllib2.Request(url)
    img = urllib2.urlopen(request).read()
    with open ('test.jpg', 'wb') as f:
        f.write(img)

download_web_image("http://192.168.0.179:8069/web/content/ir.attachment/574/datas/AWODESTEST.jpeg")
