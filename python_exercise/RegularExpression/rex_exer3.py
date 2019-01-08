import urllib.request
import re

base_url = "http://web.eecs.umich.edu/~radev/coursera-slides/"

html = urllib.request.urlopen(base_url)
html_contents = str(html.read().decode("cp949"))

url_list = re.findall(r"nlp[0-9a-zA-ZW_W.]")
