import requests
url = 'https://www.connectorride.mobi/Account/Login'
#payload = {'key1': 'value1', 'key2': 'value2'}

# GET
r = requests.get(url)

# GET with params in URL
#r = requests.get(url, params=payload)

# POST with form-encoded data
#r = requests.post(url, data=payload)

# POST with JSON 
import json
#r = requests.post(url, data=json.dumps(payload))

# Response, status etc
#print "Text" + r.text
#print "Status" + r.status_code

tokens = r.text.split(' ')
reqVerToken = tokens[tokens.index("name=\"__RequestVerificationToken\"") + 2][7:-1]

payload = { "__RequestVerificationToken": reqVerToken, 'ComputerTypes': 'PublicComputer', 'UserName': 'GIPATIL', 'Password': 'Ar3eN@!Fc' }
print payload['__RequestVerificationToken']
r = requests.post(url, data=payload)

print r.status_code