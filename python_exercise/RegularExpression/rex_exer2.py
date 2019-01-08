import urllib.request
import re

url = "https://www.google.com/googlebooks/uspto-patents-grants-text.html"
html = urllib.request.urlopen(url)
html_contents = str(html.read().decode("cp949"))

print(html_contents)

url_list = re.findall(r"(http:)(.+)(zip)",html_contents)
for url in url_list:
    print ("".join(url))
