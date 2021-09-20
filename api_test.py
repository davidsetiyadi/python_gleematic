import json
import requests
import sys

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
print ('test',res)
print (res.text)
# response = requests.request("POST", AUTH_URL, headers=headers, data=params)
params2 = {'username':'sgeede','token':'j43kFzt52SKEQ5cXDtPPpRhQXnwm24','db':'14_AW','name':'David Odestest','client_id':'123123sdxd'}
AUTH_URL2 = 'http://192.168.0.179:8069/api/post/crm_data/'
response = requests.get(
    AUTH_URL2, 
    params=params2
)
print ('test',response)
print (response.text)
# datas = response.json()