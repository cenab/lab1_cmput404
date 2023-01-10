import requests

## version number of requests library
print("Version number of requests: " + requests.__version__)

## google request printed
print(requests.get("http://google.com/").text)


##  github repo prints itselves
print(requests.get("https://raw.githubusercontent.com/cenab/lab1_cmput404/main/run.py").text)



