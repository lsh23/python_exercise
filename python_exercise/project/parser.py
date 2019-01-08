from bs4 import BeautifulSoup
import re
import sys
import io
from urllib.request import urlopen

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

search_url = "https://search.joins.com/TotalNews?Keyword=%EC%95%BC%EA%B5%AC&SortType=New&SearchCategoryType=TotalNews&PeriodType=All&ScopeType=All&ImageType=All&JplusType=All&BlogType=All&ImageSearchType=Image&TotalCount=0&StartCount=0&IsChosung=False&IssueCategoryType=All&IsDuplicate=True&Page=1&PageSize=10&IsNeedTotalCount=True"
html = urlopen(search_url)
html_contents = str(html.read().decode('utf-8'))
type(html_contents)
stock_results = re.findall("https://news.joins.com/article/\d\d\d\d\d\d\d\d")


# a = soup.find_all("div", id="article_body")
# print(a)
