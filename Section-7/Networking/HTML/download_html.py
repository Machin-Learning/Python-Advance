import urllib.request


try:
    url = urllib.request.urlopen("https://www.python.org/")
    contant = url.read()
    url.close()

except urllib.error.HTTPError:
    print("Page not Found")
    exit()

f = open("python.html","w")
f.write(str(contant))
f.close()