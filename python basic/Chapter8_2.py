#Chapter 8-2
#파이썬 외장(External) 함수
#실제 프로그램 개발 중 자주 사용
#종류 : sys, pickle, shutil, temfile, time, random 등

# EX 1
import sys
print(sys.argv)

# EX 2(강제 종료)
#sys.exit()

# EX 3(파이썬 패키지 위치)
print(sys.path)
print()


# EX 4(쓰기)
#pickle : 객체 파일 읽기, 쓰기 (저장장치에 쓰고 읽을 때 사용)
import pickle

f = open('test.obj', 'wb') # w: write, b : binary
obj = {1: 'pyhthon', 2:'study', 3:'basic'}
pickle.dump(obj, f) #dump : 파일에 원하는 내용 쓸 때 사용
f.close() #C처럼 파일을 열으면 무조건 닫아야 함

# EX 5(읽기)
f = open('test.obj', 'rb') # r : read
data = pickle.load(f) #파일을 읽을 때 사용
print(data, type(data))
f.close()
print()

# EX 6
# os : 환경 변수, 디렉터리(파일) 처리 관련, 운영체제 작업 관련
# mkdir, rmdir (비어 있으면 삭제), rename
import os

print(os.environ) #운영체제에 대한 환경 정보 출력
print(os.environ["USERNAME"])
print(os.environ["ATOM_HOME"])
print()

# 현재 경로
print(os.getcwd()) #현재 파이썬이 실행되고 있는 폴더의 결로 출력
print()

# EX 8
#time : 시간 관련 처리
import time
print(time.time())

# 형태 변환
print(time.localtime(time.time())) #현재 날짜와 시간을 모두 분해해서 보여줌(보기 편함)

# 간단 표현
print(time.ctime())

# 형식 설정
print(time.strftime('%y-%m-%d %H:%M:%S')) #%y :year, %m : month, %d : day, %H : hour, %M : minute, %S : second

# 시간 간격 발생
for i in range(6):
    print(i)
    #time.sleep(1)
print()

# EX 13
# random : 난수 리턴
import random
print(random.random()) #0 ~ 1 사이의 실수

print(random.randint(1, 45)) #1 ~ 45
print(random.randrange(1,45)) #1 ~ 44(이전에 배운 range와 같음)

d = [1,2,3,4,5]
random.shuffle(d) #섞기
print(d)

c = random.choice(d) #랜덤 뽑기
print(c)
print()

# EX 14
#webbrowser : 본인 OS의 웹브라우저 실행
import webbrowser
webbrowser.open('http://naver.com')
webbrowser.open_new('http://naver.com')
