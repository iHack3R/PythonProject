import urllib.request

url1 = "https://www.example.com/"
url2 = "https://www.example.org/"

response1 = urllib.request.urlopen(url1)
response2 = urllib.request.urlopen(url2)

if response1.getcode() != response2.getcode():
    print("The response codes are different")
    print("Response code for {}: {}".format(url1, response1.getcode()))
    print("Response code for {}: {}".format(url2, response2.getcode()))
else:
    body1 = response1.read().decode('utf-8')
    body2 = response2.read().decode('utf-8')

    if body1 == body2:
        print("The response bodies are identical")
    else:
        print("The response bodies are different")