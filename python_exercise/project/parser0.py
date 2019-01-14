from bs4 import BeautifulSoup
import re
import sys
import io
from urllib.request import urlopen

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

# def get_cleaned_text(text):
    # text = re.sub('\W+','', text.lower() )
    # return text

# def make_list_keyward_article_address (keyward) :
    search_url = "검색창결과주소"
    html = urlopen(search_url)
    html_contents = str(html.read().decode('utf-8'))
    type(html_contents)
    article_urls = re.findall("https://news.joins.com/article/\d\d\d\d\d\d\d\d 기사들의 주소를 정규표현으로 표현",html_contents)
    return article_urls


# def parsing_article (article_url) :
    html = urlopen(search_url)
    soup = BeautifulSoup(html,'html.parser')
    article_text = soup.find_all("div","post_ct")
    # article_title = soup.find_all("h1","headline mg")
    article_text = article_text[0].text
    article_text
    # article_title = article_title[0].text
    title = get_cleaned_text(article_title)
    article_data = [title,article_text]
    return article_data


def article_saver (keyward, article_data) :
    #해당 keyward폴더가 있으면 그안에 생성, 없으면 만들고 생성하는 코드 추가해야함
    with open("./"+article_data[0]+".txt",'w') as savearticle:
        savearticle.write(article_data[1])
