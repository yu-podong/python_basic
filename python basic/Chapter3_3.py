#Chaper 3-3
#파이썬 리스트
#자로구조에서 중요
#리스트 자료형(순서O, 중복O, 수정O, 삭제O)

#선언
a = []
b = list()
c = [70, 75, 80, 85]
d = [1000, 10000, 'Ace', 'Base', 'Captine']
e = [1000, 10000, ['Ace', 'Base', 'Captine']]   #다른 데이터 타입으로 선언 가능
f = [21.42, 'foobar', 3, 4, False, 3.14159]

#인덱싱
print('d - ', type(d), d)
print('d - ', d[1])
print('d - ', d[0] + d[1] + d[1])
print('d - ', d[-1])
print('e - ', e[-1][1])
print('e - ', list(e[-1][1]))
print()

#슬라이싱
print('d - ', d[0:3])
print('d - ', d[2:])
print('e - ', e[-1][1:3])
print()

#리스트 연산
print('c + d : ', c + d)
print('c * 3 : ', c * 3)
print("'Test' + c[0] : ", 'Test' + str(c[0])) #문자열 + 숫자형 불가 >>숫자형을 형 변환
print()

#값 비교
print(c == c[:3] + c[3:])
print(c)
print(c[:3] + c[3:])
print()

#Identity(id)
temp = c
print(temp, c)
print(id(temp), id(c))
print()

#리스트 수정, 삭제 !!
c[0] = 4
print('c - ', c)
c[1:2] = ['a', 'b', 'c'] #[['a', 'b', 'c']] : 리스트 안의 리스트로 삽입
print('c - ', c)
c[1] = ['a', 'b', 'c'] #리스트 안의 리스트
print('c - ', c)
c[1:3] = [] #해당 요소 삭제
print('c - ', c)
del c[2]
print('c - ', c)
print()

#리스트 함수
a = [5, 2, 3, 1, 4]
print('a - ', a)

a.append(10) #끝 부분에 데이터 삽입
print('a - ', a)

a.sort() #오름차순으로 요소 정렬 (숫자, 문자 가능)
print('a - ', a)

a.reverse() #리스트 안의 요소들을 역순으로 출력
print('a - ', a)

print('a - ', a.index(3), a[3]) #리스트에서 지정 인덱스에 해당하는 요소 출력

a.insert(2,7) #첫번째 숫자에 해당하는 인덱스에 원하는 요소 추가
print('a - ', a)

a.remove(10) #리스트 요소 중 해당 값을 삭제
print('a - ', a)

print('a - ', a.pop()) #마지막 뭔소를 가져오고 해당 원소를 제외한 리스트로 다시 구성
print('a - ', a)

print('a - ', a.count(4)) #리스트에서 해당 값과 같은 요소의 개수를 출력

ex = [8, 9]
a.extend(ex) #리스크 끝부분에 해당 리스크를 이어붙임
print('a - ', a)

#삭제 : remove, pop, del

#반복문 활용
while a:
    data = a.pop()
    print(data)
