import random
import urllib.request
from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd
from quiz00 import Quiz00
from domains import myRandom
class Quiz20:

    def quiz20list(self) -> str:
        return None

    def quiz21tuple(self) -> str:
        return None

    def quiz22dict(self) -> str:
        return None

    def quiz23listcom(self) -> str:
        print('---------- legacy ----------')
        a = []
        for i in range(5):
            a.append(i)
        print(a)
        print('---------- comprehension ----------')
        a2 = [i for i in range(5)]
        print(a2)
        return None

    def quiz24zip(self) -> str:
        url = 'https://music.bugs.co.kr/chart/track/realtime/total'
        html_doc = urlopen(url)
        soup = BeautifulSoup(html_doc, 'lxml')  # html.parser vs lxml
        ls1 = self.find_music(soup, 'title')
        ls2 = self.find_music(soup, 'artist')
        a = [i if i==0 or i==0 else i for i in range(1)]
        b = [i if i==0 or i==0 else i for i in []]
        c= [(i,j) for i,j in enumerate([])]
        b= {i:j for  i,j in zip(ls1,ls2)}
        l = [i + j for i, j in zip(ls1, ls2)]
        ls2 = list(zip(ls1,ls2))
        d1 = dict(zip(ls1,ls2))
        print(d1)
        return None

    @staticmethod
    def dict1(ls1, ls2) -> None:
        dt = {}
        for i in range(0, len(ls1)):
            print(type(f'타입: {ls1[i]}'))
            dt[ls1[i]] = ls2[i]
        print(dt)

    @staticmethod
    def dict2(ls1, ls2) -> None:
        dt = {}
        for i, j in enumerate(ls1):
            dt[j] = ls2[i]
        print(dt)

    @staticmethod
    def dict3(ls1, ls2) -> None:
        dt = {}
        for i, j in zip(ls1, ls2):
            dt[i] = j
        print(dt)

    def print_music_list(self, soup) -> None:
        artists = soup.find_all('p', {'class': 'artist'})
        # print(type(artists)) # <class 'bs4.element.ResultSet'>
        artists = [i.get_text() for i in artists]
        # print(type(artists))
        print(''.join(i for i in artists))
        titles = soup.find_all('p', {'class': 'title'})
        titles = [i.get_text() for i in titles]
        print(''.join(i for i in titles))

    def find_rank(self, soup):
        for i, j in enumerate(['artist', 'title']):
            for i, j in enumerate(self.find_music(soup, j)):
                print(f'{i}위 : {j}')
            print('#' * 100)

    @staticmethod
    def find_music(soup, cls_nm) -> []:
        ls = soup.find_all('p', {'class': cls_nm})
        return [i.get_text() for i in ls]

    def print_music_list(self, soup):
        artists = soup.find_all('p', {'class': 'artist'})
        # print(type(artists)) # <class 'bs4.element.ResultSet'>
        artists = [i.get_text() for i in artists]
        # print(type(artists))
        print(''.join(i for i in artists))
        titles = soup.find_all('p', {'class': 'title'})
        titles = [i.get_text() for i in titles]
        print(''.join(i for i in titles))

    def find_rank(self, soup):
        for i, j in enumerate(['artist', 'title']):
            for i, j in enumerate(self.find_music(soup, j)):
                print(f'{i}위 : {j}')
            print('#' * 100)

    @staticmethod
    def find_music(soup, cls_nm) -> []:
        ls = soup.find_all('p', {'class': cls_nm})
        return [i.get_text() for i in ls]

    def quiz25dictcom(self) -> str:
        # memberlsit()[myRandom(0, 23)] 이것이 1명인데 5명 추출
        # scores 는 0~100점 사이에서 랜덤
        q = Quiz00()
        c = set([q.quiz06memberChoice() for i in range(5)])
        while len(c) != 5:
            c.add(q.quiz06memberChoice())
        students = list(c)
        scores = [myRandom(0, 101) for i in range(5)]
        return {i: j for i, j in zip(students, scores)}
        print(c)
    def quiz26map(self) -> str:
        return None

    def quiz27melon(self) -> str:
        headers = {'User-Agent': 'Mozilla/5.0'}
        url = 'https://www.melon.com/chart/index.htm?dayTime=2022030816'
        req = urllib.request.Request(url, headers=headers)
        soup = BeautifulSoup(urlopen(req).read(), 'lxml')
        '''
        a = [i if i == 0 or i ==0 else i for i in range()]
        b = [ i if i ==0 or i ==0 else i for i in []]
        c = [(i,j) for i,j in enumerate([])]
        d = ''.join(i for i in [])
        '''
        return None

    def quiz28dataframe(self) -> str:
        dt = self.quiz24zip()
        df = pd.DataFrame.from_dict(dt,orient='index')
        soup = BeautifulSoup()
        print(df)
        df.to_csv('/save/bugs.csv', sep=',', na_rep='NaN')
        return None
        '''
        다음 결과 출력
            a   b   c
        1   1   3   5
        2   2   4   6
        '''
    def quiz29_pandas_01(self) -> object:
        aa = []
        bb = []
        columns = [chr(i) for i in range(97, 100)]
        [aa.append(i) if i % 2 == 0 else bb.append(i) for i in range(1, 7)]
        d = {'1': bb, '2': aa}
        df3 = pd.DataFrame.from_dict(d, orient='index', columns=columns)

        print(df3)


