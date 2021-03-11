#Chapter 3-4
#파이썬 튜플
#리스트와 비교 중요
#튜플 자료형(순서O, 중복O, 수정X, 삭제X) -> 불변(변경되면 안돼는 값)

#선언
a = ()
b = (1,)    #원소가 하나일 떄 int형으로 인식, 원소 하나일 때 끝에 , 사용 :tuple로 인식
c = (11, 12, 13, 14)
d = (100, 1000, 'Ace', 'Base', 'Captine')
e = (100, 1000, ('Ace', 'Base', 'Captine'))

#인덱싱
print('d - ', d[1])
print('d - ', d[1] + d[1])
print('d - ', d[-1])
print('e - ', e[-1])
print('e - ', e[-1][1])
print('e - ', list(e[-1][1])) #튜플 -> 리스트 형 변환 가능, 이때 리스트의 특징을 갖게 됨
print()

#수정X
"""d[0] = 1500 #에러 발생 """

#슬라이싱
print('d - ', d[0:3])
print('d - ', d[2:])
print('e - ', e[2][1:3])
print()

#튜플 연산
#내부의 원소가 변경 or 삭제 X -> 연산을 통해 원소의 개수 증가 허용
print('c + d : ', c + d)
print('c * 3 : ', c * 3)
print('Test + d[2] : ', 'Test ' + d[2])
print()

#튜플 함수
a = (5, 1, 2, 3, 4)
print('a - ', a)
print('a - ', a.index(3))
print('a - ', a.count(2))
print()

#팩킹 & 언팩킹 (Packing & Unpacking)

#팩킹 : 하나로 묶다
t = ('foo', 'bar', 'baz', 'qux')
print(t)
print(t[0])
print(t[-1])
print()

#언팩킹
(x1, x2, x3, x4) = t #팩킹되어 있던 것을 각 변수로 할당 -> 언팩킹(괄호 없어도 가능)

print(type(x1), type(x2), type(x3), type(x4))
print(x1, x2, x3, x4)

t2 = 1, 2, 3
t3 = 4,
x1, x2, x3 = t2
x4, x5, x6 = 4, 5, 6

print(t2)
print(t3)
print(x1, x2, x3)
print(x4, x5, x6)
