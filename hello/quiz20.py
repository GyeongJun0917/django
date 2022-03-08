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
        soup = BeautifulSoup(html_doc, 'lxml')
        artists = soup.find_all('p', {'class':'artist'})
        artists = [i.get_text() for i in artists]
        print(''.json(i for i in artists))
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
        herders = {'User-Agent': 'Mozilla/5.0'}
        url = 'https://www.melon.com/chart/index.htm?dayTime=2022030816'
        req = urllib.request.Request(url, herders=herders)
        soup = BeautifulSoup(urlopen(req).read(), 'lxml')


        return None

    def quiz28(self) -> str: return None

    def quiz29(self) -> str: return None

