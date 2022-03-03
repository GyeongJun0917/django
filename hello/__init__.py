from hello.domains import Member
from hello.models import Quiz01Calculator, Quiz02Bmi, Quiz03Grade, Quiz04GradeAuto, Quiz05Dice, Quiz06RandomGenerator, Quiz07RandomChoice, Quiz08Rps, Quiz09GetPrime, Quiz10LeapYear, Quiz11NumberGolf, Quiz12Lotto, Quiz13Bank, Quiz14Gugudan
import random
if __name__ == '__main__':
    while 1:
        menu = input('0.Exit 1.계산기(+, -, *, /) 2. BMi계산 3.성적표 4. 성적표 자동, 5. 주사위'
                     '6. 랜덤정수 7.803호 랜덤 8.가위바위보')
        if menu == 0:
            break
        elif menu == '1':
            calc = Quiz01Calculator(int(input('첫번째 수')), int(input('두번째 수')), input('+, -, *, /'))
            print(('*'*30)+f'\n{calc.num1}{calc.opcode}{calc.num2}={calc.calc_res()}\n'+('*'*30))

        elif menu == '2':
           member = Member()
           q2 = Quiz02Bmi
           member.name = input('이름 :')
           member.height = float(input('키 : '))
           member.weight = float(input('몸무게 : '))
           res = q2.getBmi(member)
           print(f'이름:{member.name}, 키: {member.height}, 몸무게: {member.weight}, BMI상태: {res}')

        elif menu == '3':
            grade = Quiz03Grade(input('이름'), int(input('국어점수')), int(input('영어점수')), int(input('수학점수')))
            print(('#' * 30) + '\n'
                               f'이름: {grade.name}\n국어: {grade.kor}점\n'
                               f'영어: {grade.eng}점\n수학: {grade.math}점\n'
                               f'총점: {grade.total()}점\n 평균: {grade.avg()}점\n'
                               f'합격여부: {grade.grade_pass()}\n'
                  + ('#' * 30))

        elif menu == '4':
            q4 = Quiz04GradeAuto()
            break

        elif menu == '5':
            print(Quiz05Dice.cast())

        elif menu == '6':
            q6Random = None

        elif menu == '7':
            print(Quiz07RandomChoice.choiceMembers())

        elif menu == '8':
            q8rps = Quiz08Rps(int(input('가위 1 바위 2 보3')))
            print(f'플레이어: {q8rps.player} 컴퓨터: {q8rps.com()} 게임결과 : {q8rps.game()}')

        elif menu == '9':
            break

        elif menu == '10':
            q10 = Quiz10LeapYear(int(input('연도를 입력하세요')))
            print(q10.leapYear())

        elif menu == '11':
            q11 = Quiz11NumberGolf(int(input('1~100까지 입력하세요')))
            print(q11.game())

class Quiz01Calculator(object):

    def __init__(self, num1, num2, opcode):
        self.num1 = num1
        self.num2 = num2
        self.opcode = opcode

    def calc_res(self):
        if self.opcode == '+':
            return self.num1 + self.num2
        elif self.opcode == '-':
            return self.num1 - self.num2
        elif self.opcode == '*':
            return self.num1 * self.num2
        elif self.opcode == '/':
            return self.num1 / self.num2


class Quiz02Bmi(object):
    @staticmethod
    def getBmi(member):
        this = member
        bmires = this.weight / (this.height * this.height)*10000
        if bmires < 18.5:
            return '저체중'
        elif bmires < 23:
            return '정상'
        elif bmires < 25:
            return '과체중'
        elif bmires < 30:
            return '경도 비만(1단계 비만)'
        elif bmires < 35:
            return '중도 비만(2단계 비만)'
        else:
            return '고도 비만'
class Quiz03Grade(object):

    def __init__(self, kor, eng, math, name):
        self.kor = kor
        self.eng = eng
        self.math = math
        self.name = name

    def total(self):
        return self.kor + self.eng + self.math

    def avg(self):
        return self.total() / 3

    def grade_pass(self):
        return '합격' if self.avg() >= 60 else '불합격'

class Quiz04GradeAuto(object):
    def __init__(self, name, kor, eng, math):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math

    def total(self):
        return self.kor + self.eng + self.math
    def avg(self):
        return self.total()/3
    def grade_pass(self):
        return '합격' if self.avg() >= 60 else '불합격'

def myRandom(start, end):
    return random.randint(start, end)

class Quiz05Dice(object):
    @staticmethod
    def cast():
        return myRandom(1, 6)

class Quiz06RandomGenerator(object): # 원하는 범위의 정수에서 랜덤값 1개 추출
    @staticmethod
    def cast():
        pass

class Quiz07RandomChoice(object): # 803호에서 랜덤으로 1명 이름 추출
     @staticmethod
     def choiceMembers():
         members = ['홍정명', '노홍주', '전종현', '정경준', '양정오',
                        "권혜민", "서성민", "조현국", "김한슬", "김진영",
                        '심민혜', '권솔이', '김지혜', '하진희', '최은아',
                        '최민서', '한성수', '김윤섭', '김승현',
                        "강 민", "최건일", "유재혁", "김아름", "장원종"]
         return random.choice(members)


class Quiz08Rps(object): # 1.가위 2.바위 3.보
    def __init__(self, player):
        self.player = player
    def com(self):
        return myRandom(1, 3)

    def game(self):
        p = self.player
        c = self.com()

        if p == c:
            res = '무승부'
        elif (p == 1 and c == 3) or (p == 2 and c == 1) or (p == 3 and c == 2):
            res = '승리'
        else:
            res = '패배'
        return res



class Quiz09GetPrime(object):
    def __init__(self, number):
        self.number = number

class Quiz10LeapYear(object):
    def __init__(self, year):
        self.year = year
    def leapYear(self):
        a = self.year
        if a%4==0 and a%100!=0 or a%400==0:
            return '윤년'
        else:
            return '평년'


class Quiz11NumberGolf(object):
    def __init__(self, player):
        self.player = player
    def com(self):
        return myRandom(1, 100)

    def game(self):
        p = self.player
        c = self.com()
        while p != c:
            if p >= 100:
                return '숫자 다시 입력'
            elif c > p:
                return 'up'
            elif c < p:
                return 'down'
        return '정답입니다'


class Quiz12Lotto(object):
    def __init__(self):
        pass

class Quiz13Bank(object): # 이름, 입금, 출금만 구현
    def __init__(self):
        pass

class Quiz14Gugudan(object): # 책받침구구단
    def __init__(self):
        pass




