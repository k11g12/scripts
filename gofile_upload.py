# -*- coding: utf-8 -*-

import requests
import datetime
import sys

"""
import logging

try:
    import http.client as http_client
except ImportError:
    # Python 2
    import httplib as http_client
http_client.HTTPConnection.debuglevel = 1


# You must initialize logging, otherwise you'll not see debug output.
logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)
requests_log = logging.getLogger("requests.packages.urllib3")
requests_log.setLevel(logging.DEBUG)
requests_log.propagate = True
"""

doc_url = "https://docs.google.com/document/export?format=pdf&id=1lh5VBnVeY-XDBENyjhJlawlcyfaUpACsEJrjSb3ldH4"

r = requests.get(doc_url)
filename = '/tmp/formosahuasca.pdf'

with open('/tmp/formosahuasca.pdf', 'wb') as f:
    f.write(r.content)

print("download pdf done")

description = "台灣相思湯指南"

indays = int(sys.argv[1])

expire = (datetime.datetime.now() + datetime.timedelta(days=indays)).strftime('%Y-%m-%d')

url = "https://gofile.io/ajax/upload.php"

files = {'file[]': ("台灣相思湯指南Formosahuasca.pdf", open(filename, 'rb'),'application/pdf')}

data = {
        'comments': 0,
        'description': description,
        'category': 'file',
        'expire': expire
        }

#print(data)

r = requests.post(url, files=files, data=data)

result = r.text.split(";")

file_id = result[1]
link = "https://gofile.io/?c="+file_id
key = result[2]

print file_id
print link
print key
