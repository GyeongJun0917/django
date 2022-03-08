import typing

from numpy.random.mtrand import random

from hello import Member
from hello.domains import my100, myRandom, memberlist


class Quiz00:
    def quiz00calculator(self):
        n1 = myRandom(1, 100)
        n2 = myRandom(1, 100)
        o = ['+', '-', '*', '/', '%']
        op = o[myRandom(0, 4)]

        if (op == '+'):
            res = n1 + n2
        elif (op == '-'):
            res = n1 - n2
        elif (op == '*'):
            res = n1 * n2
        elif (op == '/'):
            res = n1 / n2
        elif (op == '%'):
            res = n1 % n2

        return print(f'{n1} {op} {n2} = {res}')

    def quiz01bmi(self):
        this = Member()
        this.name = memberlist()
        this.inch = myRandom(120, 200)
        this.weight =myRandom(40, 120)
        bmi = this.weight / (this.inch * this.inch / 10000)
        name = this.name[myRandom(0, 4)]
        if bmi <= 18.0:
            res = '저체중'
        elif bmi <= 22.9:
            res = '정상'
        elif bmi <= 23.0:
            res = '과체중'
        elif bmi <= 24.9:
            res = '위험체중'
        elif bmi <= 29.9:
            res = '결과: 1단계 비만'
        elif bmi <= 34.9:
            res = '결과: 2단계 비만'
        elif bmi < 35:
            res = '결과: 고도 비만'
        return print(f'이름:{name}\n 키:{this.inch}\n 몸무게:{this.weight}\n Bmi지수:{bmi}\n 결과:{res} ')

    def quiz02dice(self):
            dice1 = myRandom(1, 6)
            dice2 = myRandom(1, 6)
            if dice1 > dice2:
                res = f'1번 주사위{dice1}\n 2번주사위:{dice2}\n 1번 주사위가 {dice1 - dice2}차이로 이겼다'
            elif dice1 < dice2:
                res = f'1번 주사위: {dice1}\n 2번주사위: {dice2}\n2번 주사위가 {dice2 - dice1}차이로 이겼다'
            else:
                res = '비겼다'
            return print(res)

    def quiz03rps(self):
            c = myRandom(0, 2)
            p = myRandom(0, 2)
            rps = ['가위', '바위', '보']

            if p - c == 2 or c - p == -1:
                res = 'WIN'
            elif p - c == 1 or c - p == -2:
                res = 'LOSE'
            elif p - c == 0:
                res = 'DRAW'
            return print(f'플레이어: {rps[p]}\n 컴퓨터:{rps[c]}\n 결과: {res}')

    '''
    <게이머 승리일때>
     컴퓨터0(가위) / 게이머1(바위)(win) = -1
     컴퓨터1(바위) / 게이머2(보)(win) = -1
     컴퓨터2(보) / 게이머0(가위)(win) = 2
    <컴퓨터 승리일때>
     컴퓨터0(가위) / 게이머2(보)(lose) = -2
     컴퓨터1(바위) / 게이머0(가위)(lose) = 1
     컴퓨터2(보) / 게이머1(바위)(lose) = 1 '''

    def quiz04leap(self):
        y = myRandom(0, 2022)
        return print(f'{y}년은 윤년') if (y % 4 == 0 and not y % 100 == 0 or y % 400 == 0) else  print(f'{y}년은 평년')

    def quiz05grade(self):
        name = memberlist()
        kor = myRandom(0, 100)
        eng = myRandom(0, 100)
        math = myRandom(0, 100)
        total = kor + eng + math
        avg = total / 3
        if avg >= 90:
            grade = 'A'
        elif avg >= 80:
            grade = 'B'
        elif avg >= 70:
            grade = 'C'
        elif avg >= 65:
            grade = 'D'
        elif avg >= 60:
            grade = 'E'
        else:
            grade = 'F'
            if grade == 'F':
                grpass = '불합격'
            else:
                grpass = '합격'

        return print(f'########## 성적표 ########\n '
                     f'* 이름: {name}\n  '
                     f'* > 국어: {kor}점\n  '
                     f'* > 영어: {eng}점\n" '
                     f'* > 수학: {math}점\n '
                     f'* 총점: {total}점\n '
                     f'* 평균(정수): {avg}점\n'
                     f'* 학점: {grade}\n'
                     f'합격여부: {grpass}\n'
                     '* #######################')

    def quiz06memberChoice(self):
        return memberlist()[myRandom(0, 23)]

    def quiz07lotto(self):
        lotto = random.sample(range(1, 45), 6)
        return lotto.sort()

    def quiz08bank(self): # 이름, 입금, 출금만 구현
        Account.main()

    def quiz09gugudan(self):  # 책받침구구단
        res = ""
        for i in [2, 6]:
            for j in range(1, 10):
                for k in range(0, 4):
                    res += f'{i + k} * {j} = {(i + k) * j}\t'
                res += '\n'
            res += '\n'
        return print(res)


'''
은행이름은 비트은행
입금자 이름(name), 계좌번호(account_number), 금액(money) 속성값으로 계좌를 생성한다.
계좌번호는 3자리-2자리-6자리 형태로 랜덤하게 생성된다.
123-12-123456
'''
class Account(object):
    def __init__(self, name, account_number, money):
        self.BANK_NAME = '비트은행'
        self.name = Quiz00().quiz06memberChoice() if name == None else name
       # self.acc_num =f'{myRandom(0, 100): 0>3}-{myRandom(0, 1000): 0>2}-{myRandom(0, 1000000): 0>6}'
        self.account_number = self.creat_account_number() if account_number == None else account_number
        self.money = myRandom(100, 1000) if money == None else money

    def to_string(self):
        return f'** 은행 : {self.BANK_NAME}\n' \
               f'** 입금자 : {self.name}\n' \
               f'** 계좌번호 : {self.account_number}\n' \
               f'** 금액 : {int(self.money)} 만원'
    def creat_account_number(self):
     '''
        ls = [str(myRandom(0,10))for i in range(3)]
        ls = ls.append("-")
        ls = [str(myRandom(0,10)) for i in range(2)]
        ls = ls.append("-")
        ls = [str(myRandom(0,10)) for i in range(6)]

     '''
     return "".join('-' if i==3 or i==6 else str(myRandom(0,10)) for i in range(13))

    @staticmethod
    def deposit(ls, account_number, deposit):
        j = []
        for i,j in enumerate(ls):
            if j.account_number == account_number:
                j.money += deposit
                print(ls[i].to_string())
                '''
                print(f'계좌번호 :{account_number}\n'
                      f'입금액 :{deposit}만원이 입금되었습니다.\n '
                      f'잔액 :{j.money}만원\n')
                '''

    @staticmethod
    def wif(ls, account_number, money):
        for i,j in enumerate(ls):
            if j.account_number == account_number:
                if(j.money - money) < 0 :
                    print(f'잔액이 부족합니다.')
                else:
                    j.money -= money
                    print(ls[i].to_string())
                    '''
                    print(f'계좌번호 : {account_number}\n'
                          f'출금액 : {money}만원이 출금되었습니다\n'
                          f'잔액 : {j.money}만원\n')
                    '''


    @staticmethod
    def find_account(ls, account_number):
        #return ''.join([j.to_string() if j.account_number == account_number else '찾는 계좌 아님' for i, j in enumerate(ls)])
        for i, j in enumerate(ls):
            if j.account_number == account_number:
                a = ls[i]
        return a
    @staticmethod
    def del_account(ls, account_number):
        for i, j in enumerate(ls):
            if j.account_number == account_number:
                del ls[i]

    @staticmethod
    def main():
        ls = []
        while 1:
            menu = input('0.종료 1.계좌개설 2.계좌목록 3.입금 4.출금 5.계좌해지 6.계좌조회')
            if menu == '0':
                break
            if menu == '1':
                acc = Account(None, None, None)
                print(f'{acc.to_string()} ... 개설되었습니다.')
                ls.append(acc)
            elif menu == '2':
                a = '\n'.join(i.to_string() for i in ls)
                print(a)
            elif menu == '3':
                Account.deposit(ls, input('입금할 계좌번호'), int(input('입금액')))

            elif menu == '4':
                Account.wif(ls, input('출금할 계좌번호'),int(input('출금액')))
                # 추가코드 완성
            elif menu == '5':
                Account.del_account(ls, input('탈퇴할 계좌번호'))
            elif menu == '6':
                print(Account.find_account(ls, input('검색할 계좌번호')))
            else:
                print('Wrong Number.. Try Again')
                continue



