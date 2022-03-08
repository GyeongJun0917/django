import random
import urllib.request
from urllib.request import urlopen

from bs4 import BeautifulSoup

class Quiz20:

    def quiz20list(self) -> str: return None

    def quiz21tuple(self) -> str: return None

    def quiz22dict(self) -> str: return None

    def quiz23listcom(self) -> str:
        print('-----------legacy-----------')
        a = []
        for i in range(5):
            a.append(i)
        print(a)
        print('-----------comprehension-----------')
        a2 = [i for  i in range(5)]
        print(a2)


    def quiz24zip(self) -> str:
        url = 'https://music.bugs.co.kr/chart/track/realtime/total'
        html_doc = urlopen(url)
        soup = BeautifulSoup(html_doc, 'lxml')  # html.parser vs lxml
        # print(soup.prettify())
        # artist = soup.find_all(attrs={'class':'artist'})
        print('\n'.join([i.get_text().strip() for i in soup.find_all('p', {'class': 'artist'})][0:3]))
        # print(type(artists))
        return None
        # print(soup.find_all('p', class_="artist")[0].text)
        '''
        trs = soup.select("#CHARTrealtime > table > tbody > tr")
        for tr in trs:
            title_a = tr.select_one("th")
            if title_a is not None:
                print(title_a.text)
        '''



        #print(soup.prettify())


    def quiz25dictcom(self) -> str: return None

    def quiz26(self) -> str: return None

    def quiz27melon(self) -> str:
        headers = {'User-Agent': 'Mozilla/5.0'}
        url = 'https://www.melon.com/chart/index.htm?dayTime=2022030816'
        req = urllib.request.Request(url, headers=headers)
        soup = BeautifulSoup(urlopen(req).read(), 'lxml')
        print(''.join(i.get_text() for i in soup.find_all('div', {'class': 'ellipsis rank01'})[0:3]))
        return None

    def quiz28(self) -> str: return None

    def quiz29(self) -> str: return None

