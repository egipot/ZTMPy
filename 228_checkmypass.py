# https://passwordsgenerator.net/sha1-hash-generator/
# https://pypi.org/project/requests/ 

import requests

#url = 'https://api.pwnedpasswords.com/range' + 'password123'
#url = 'https://api.pwnedpasswords.com/range' + 'CBFDAC6008F9CAB4083784CBD1874F76618D2A97'

url = 'https://api.pwnedpasswords.com/range/' + 'CBFDA'
res = requests.get(url)
print(res)
#<Response [200]>