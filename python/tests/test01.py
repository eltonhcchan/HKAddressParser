from context import Address, Similarity # type: ignore
import json

ad = Address('禮頓道33號')
j = ad._result
msg = "Hello"
print(msg)
json_string = json.dumps(j, indent=4, ensure_ascii=False).encode('utf8')
print(json_string.decode())
print(j[0]['geo']['Northing'])
print(msg)
#result = ad.ParseAddress()
#print(result)

x = ad._inputAddr
print(x)

from json2table import convert
html=convert(json_string)
print(html)