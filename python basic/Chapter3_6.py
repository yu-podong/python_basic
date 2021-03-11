#Chapter 3-6
#집합(Sets) 특징
#집합 자료형 : 순서X, 중복X

#선언
a = set()
b = set([1, 2, 3, 4, 4, 4])
c = set([1, 4, 5, 6])
d = set([1, 2, 'Pen', 'Cap', 'Plate'])
e = {'foo', 'bar', 'baz', 'foo', 'qux'} #키 없이 사용 -> Sets 자료형
f = {42, 'foo', (1, 2, 3),3.14159}

print('a - ', type(a), a) #중북 허용X -> 같은 원소가 여려 개 있어도 하나만 출력
print('b - ', type(b), b)
print('c - ', type(c), c)
print('d - ', type(d), d)
print('e - ', type(e), e)
print('f - ', type(f), f)
print()

#튜플 변환(set -> tuple)
t = tuple(b)
print('t - ', t, type(t))
print('t - ', t[0], t[1:3])
print()

#리스트 변환(set -> list)
l = list(c)
l2 = list(e)
print('l - ', l, type(l))
print('l2 - ', l2, type(l2))

#길이
print(len(a)) #길이 == 잡합 안의 서로 다른 원소의 개수
print(len(b))
print(len(c))
print(len(d))
print(len(e))
print(len(f))
print()

#집합 자료형 활용
s1 =set([1, 2, 3, 4, 5, 6])
s2 =set([4, 5, 6, 7, 8, 9])

print('s1 & s2 : ', s1 & s2)
print('s1 & s2 : ', s1.intersection(s2))  #intersection : 교집합 합수

print('s1 | s2 : ', s1 | s2)
print('s1 | s2 : ', s1.union(s2)) #union : 합집합 함수

print('s1 - s2 : ', s1 - s2)
print('s1 - s2 : ', s1.difference(s2)) #difference : 차집합 함수
print()

#중복 원소 확인
print('s1 & s2 : ', s1.isdisjoint(s2)) #교집합O : False, 교집합X : True

#부분 집합 확인
print('subset : ', s1.issubset(s2)) #s1이 s2의 부분집합인지?
print('superset : ', s1.issuperset(s2)) #s2가 s1의 부분집합인지?
print()

#데이터 추가 & 제거
s1 = set([1, 2, 3 ,4])

s1.add(5) #원소 추가
print('s1 - ', s1)

s1.remove(2)  #없는 원소를 삭제하면 ERROR 발생
print('s1 - ', s1)

s1.discard(3) #원소 삭제 If 없는 원소 삭제 -> ERROR 발생X
print('s1 - ', s1)

s1.clear() #모든 원소 삭제
print('s1 - ', s1)
print()

a = [1, 2, 3]
a.clear()
print('a - ', a)
