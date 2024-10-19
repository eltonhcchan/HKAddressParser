from context import Address, Similarity # type: ignore
import json

ad = Address('禮頓道33號')
j = ad._result
msg = "Hello"
print(msg)
print(json.dumps(j, indent=4))
print(j[1]['geo']['Northing'])
print(msg)
#result = ad.ParseAddress()
#print(result)
