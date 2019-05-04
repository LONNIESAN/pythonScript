from bs4 import BeautifulSoup;
import requests;
import json;
import re;
from multiprocessing import Pool;


def generate_allurl(user_in_nub):
    url ='http://su.lianjia.com/ershoufang/pg{}/'
    for url_next in range(1,int(user_in_nub)):
        get_allurl(url.format(url_next));
        # yield url.format(url_next);

def get_allurl(generate_allurl):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36'}
    get_url = requests.get(generate_allurl,headers=headers)
    if get_url.status_code == 200:
        # re_set = re.compile('<li.*?class="clear">.*?<a.*?cla1ss="img".*?href="(.*?)"')
        # re_set = re.compile('<div class="title"><a target="_blank">')

        re_set = re.compile('<div class="title"><a.*? href="(.*?)"')

        # re_set = re.compile('<a hr2ef="https://su.lianjia.com/ershoufang/.*" target="_blank" .* >.*</a>')
        # re_set = re.compile('')
        re_get = re.findall(re_set, get_url.text)
        # print(get_url.text)
        print(re_get)
        for url in re_get:
            open_url(url)

def open_url(re_get):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36'}
    res = requests.get(re_get,headers=headers)
    if res.status_code == 200:
        info = {}
        soup = BeautifulSoup(res.text,'lxml')
        info['标题'] = soup.select('.main')[0].text
        info['总价'] = soup.select('.total')[0].text + '万'
        info['每平方售价'] = soup.select('.unitPriceValue')[0].text
        print(info)
        return info

def writer_to_text(list):  # 储存到text22
     with open('链家二手房.text', 'a', encoding='utf-8')as f:
         f.write(json.dumps(list, ensure_ascii=False) + '\n')
         f.close()

def main():
    user_in_nub = input('输入生成页数:')
    for i in generate_allurl(user_in_nub):
        print(i)
        # open_url(i)
    # writer_to_text(open_url(url))  # 储存到text文件


if __name__ == '__main__':
   main();