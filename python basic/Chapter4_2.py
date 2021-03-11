#Chapter 4-2
#파이썬 반복문
#for 실습

import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


#코딩의 핵심
#for in <collection>
#   <Loop body>

for v1 in range(10): #0 ~ 9,  range(start, stop, step)
    print('v1 is :', v1)
print()

for v2 in range(1,11): #1 ~ 10
    print('v2 is :', v2)
print()

for v3 in range(1, 11, 2):
    print('v3 is :', v3)
print()

#1 ~ 1000까지의 합
sum1 = 0

for v in range(1,1001):
    sum1 += v
print('1 ~ 1000 sum :', sum1)

print('1 ~ 1000 sum :', sum(range(1,1001))) #sum 함수는 내부적으로 리스트 받음
print(type(range(1,11))) #range 함수 : generator과 iterator -> 리스트 생성
print('1 ~ 1000 4의 배수의 합 :', sum(range(4,1001,4)))

#Iterables 자료형 (== 반복할 수 있는 객체) 반복
#문저열, 리스트, 튜플, 집합, 딕션너리
#iterable 리턴 함수 : range, reversed, enumerate, filter, map, zip

# EX 1
name = ['Kim', 'Park', 'Cho', 'Lee', 'Choi', 'Yoo']

for n in name: #collection의 첫 번째 요소부터 마지막 요소까지 차례로 변수에 대입
    print('You are :', n)
print()

# EX 2
lotto_numbers = [14 ,23, 66, 52, 26, 29]

for n in lotto_numbers:
    print('Current number :', n)
print()

# EX 3
word = "Beautiful"
for s in word:
    print('word :', s)
print()

# EX 4
my_info = dict(
    name = 'Lee',
    age = 33,
    city = 'Seoul'
)

for k in my_info:
    print('key :', k)
    print('value :', my_info[k]) #해당 키의 value 출력 (== my_info.get(k))
print()

for v in my_info.values():
    print('value :', v)

# EX 5
name = 'FineAppLE'

for n in name:
    if n.isupper():
        print(n)
    else:
        print(n.upper())
print()

#break
number = [14, 3 ,7, 10, 24 ,17, 2, 33, 15, 34, 36, 38]

for num in number:
    if num == 34:
        print('Found 34')
        break
    else:
        print('Not Found : ', num)
print()

#continue
lt = ["1", 2, 5, True, 4.3, complex(4)]

for v in lt:
    if type(v) is bool: #자료형 대조 시 is 사용
        continue
    print("Current type :", type(v))
print()

#for - else
number = [14, 3 ,7, 10, 24 ,17, 2, 33, 15, 34, 36, 38]

for num in number:
        if num == 55:
            print("Found 55")
            break
else:
    print('Not Found 55')
print()

#구구단
for i in range(2, 10):
    for j in range(1, 10):
        print('{:4d}'.format(i * j), end = '')
    print()
print()

#변환 예제
name2 = 'Aceman'

print('Reversed', reversed(name2)) #reversed 함수만 쓰면 변수의 주소값 출력
print('List', list(reversed(name2)))
print('List', tuple(reversed(name2)))
print('Set', set(reversed(name2))) #집합 : 순서X -> 실행할 떄마다 원소 위치가 달라짐
