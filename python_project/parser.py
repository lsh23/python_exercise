from bs4 import BeautifulSoup
import re
import sys
import io
from urllib.request import urlopen

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

def get_cleaned_text(text):
    text = re.sub('\W+','', text.lower() )
    return text

def make_list_keyward_article_address (keyward) :
    search_url = "https://search.joins.com/TotalNews?Keyword="+str(keyward)+"&SortType=New&SearchCategoryType=TotalNews&PeriodType=All&ScopeType=All&ImageType=All&JplusType=All&BlogType=All&ImageSearchType=Image&TotalCount=0&StartCount=0&IsChosung=False&IssueCategoryType=All&IsDuplicate=True&Page=1&PageSize=10&IsNeedTotalCount=True"
    html = urlopen(search_url)
    html_contents = str(html.read().decode('utf-8'))
    type(html_contents)
    article_urls = re.findall("https://news.joins.com/article/\d\d\d\d\d\d\d\d",html_contents)
    return article_urls


def parsing_article (article_url) :
    html = urlopen(article_url)
    soup = BeautifulSoup(html,'html.parser')
    article_text = soup.find_all("div","article_body")
    article_title = soup.find_all("h1","headline mg")
    article_text = article_text[0].text
    article_title = article_title[0].text
    title = get_cleaned_text(article_title)
    article_data = [title,article_text]
    return article_data


def article_saver (keyward, article_data) :
    #해당 keyward폴더가 있으면 그안에 생성, 없으면 만들고 생성하는 코드 추가해야함
    with open("./"+article_data[0]+".txt",'w') as savearticle:
        savearticle.write(article_data[1])
