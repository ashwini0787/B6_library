import requests

resp1 = requests.get("http://127.0.0.1:8000/homepage_cbv/")
print(resp1.content)

resp2 = requests.post("http://127.0.0.1:8000/homepage_cbv/" , data= {"Key": "value"} )
print(resp2.content)      # output in byte form http response

resp3 = requests.delete("http://127.0.0.1:8000/homepage_cbv/")
print(resp3.content)

resp4 = requests.put("http://127.0.0.1:8000/homepage_cbv/")
print(resp4.content)

resp5 = requests.patch("http://127.0.0.1:8000/homepage_cbv/")
print(resp5.content)