#Chapter 3-5
#파이썬 딕셔너리
#범용적으로 가장 많이 사용
#딕셔너리 자료형(순서X, 키 중복X, 수정O, 삭제O)

#선언
a = {'name' : 'Kim', 'phone' : '01011112222', 'birth' : '001122'} #키 -> 모든 자료형 가능
b = {0: 'Hello Python'}
c = {'arr' : [1, 2, 3, 4]}
d = {
    'Name' : 'Niceman',
    'City' : 'Seoul',
    'Age' : 20,
    'Grade' : 'A',
    'Status' : True
}
e = dict([
    ('Name', 'Niceman'),
    ('City', 'Seoul'),
    ('Age', 20),
    ('Grade', 'A'),
    ('Status', True)
])
f = dict(
    Name = 'Niceman',
    City = 'Seoul',
    Age = 21,
    Grade = 'A',
    Status = True
)

print('a - ', type(a), a)
print('b - ', type(b), b)
print('c - ', type(c), c)
print('d - ', type(d), d)
print('e - ', type(e), e)
print('f - ', type(f), f)
print()

#출력
print('a - ', a['name']) #키 존재X -> ERROR 발생
print('a - ', a.get('name')) #키 존재X -> None으로 출력
print('b - ', b[0])
print('b - ', b.get(0))
print('f - ', f.get('City'))
print('f - ', f.get('Age'))
print()

#딕셔너리 추가
a['address'] = 'seoul' #If 기존의 키의 내용 변경 시 원하는 내용으로 변경 가능
print('a - ', a)
a['rank'] = [1, 2, 3]
print('a - ', a)
print()

#딕셔너리 길이
print('a - ',len(a)) #딕셔너리에서 길이 == 키의 개수
print('b - ',len(b))
print('c - ',len(c))
print('d - ',len(d))
print()

##dict_keys, dict_values, dict_items : 반복문(__iter__)에서 사용 가능
print('a - ', a.keys()) #모든 키 값만 출력(내용 출력 X)
print('b - ', b.keys())
print('c - ', c.keys())
print('d - ', d.keys())

print('a - ',list(a.keys()))
print('b - ',list(b.keys()))
print()

print('a - ', a.values()) #모든 키의 내용만 출력(키 출력 X)
print('b - ', b.values())
print('c - ', c.values())
print('d - ', d.values())

print('a - ',list(a.values()))
print('b - ',list(b.values()))
print()

print('a - ', a.items()) #딕셔너리 안에 있는 모든 키와 내용들을 리스트 형태로 출력
print('b - ', b.items())
print('c - ', c.items())

print('a - ',list(a.items()))
print('b - ',list(b.items()))
print()

print('a - ', a.pop('name')) #키에 해당하는 내용을 꺼냄
print('a - ', a)
print('c - ', c.pop('arr'))
print('c - ', c)

print('f - ', f.popitem()) #임의의 데이터(키, 내용)을 꺼냄
print('f - ', f)
print()

print('a - ', 'birth' in a) #찾고자 하는 키의 유무를 확인
print('d - ', 'city' in d)

#수정 & 추가
a['test'] = 'test_dict'
print('a - ', a)
a['address'] = 'dj'
print('a - ', a)

a.update(birth = '910804') #키의 값 수정(update 함수는 반환값 void)
print('a - ', a)

temp = {'address' : 'Busan'}
a.update(temp)
