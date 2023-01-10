import requests
print("Version number of requests: " + requests.__version__)
print(requests.get("http://google.com/").text)




