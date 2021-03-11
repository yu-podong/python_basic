#Chapter 8-1
#파이썬 내장(Built-in) 함수
#자주 사용하는 함수 위주
#사용하다보면 자연스럽게 숙달

#절댓값
print(abs(-3),'\n')

#all, any : interable(ex. list, tuple) 요소 검사 (참, 거짓)
print(all([1, 2, ''])) #하나의 요소가 False에 해당하면 결과값 False (== and)
print(any([1, 2, 0]))   #True 값이 하나라도 있으면 True (== or)
print()

#chr : 아스키 -> 문자, ord : 문자 -> 아스키
print(chr(33))
print(ord('!'))
print()

#enumerate : 인덱스 + interable 객체 생성
for i, name in enumerate(['abc', 'bdc', 'efd']):
    print(i+1, name)
print()

#filter : 반복가능한 객체 요소를 지정한 함수 조건에 맞는 값 추출
def conv_pos(x):
    return abs(x) > 2
print(list(filter(conv_pos, [1, -2, 3, -4])))
print(list(filter(lambda x: abs(x)>2, [1, -2, 3, -4])))
print()

#id : 객체의 주소값(래퍼런스) 반환
print(id(int(5)))
print(id(4))
print()

#len : 요소의 길이 반환
print(len('abcdefg'))
print(len([1,2,3,4,5,6,7,8,9,0]))
print()

#max, min : interable한 요소들 중에서 최대, 최소
print(max([1,5,8,2]))
print(max('python study'))
print(min([1,5,8,2]))
print(min('pythonstudy'))
print()

#map : 반복가능한 객체 요소를 지정한 함수 실행 후 추출
def conv_abs(x):
    return abs(x)

print(list(map(conv_abs, [1, -2, 3, -4, 5])))
print(list(map(lambda x: abs(x), [1, -2, 3, -4, 5])))
print()

#pow : 제곱값 반환
print(pow(2, 10))

#range : 반복가능한 객체(interable)로 반환
print(range(1,10,2))
print(list(range(1,10,2)))
print(list(range(0,-15,-1)))
print()

#round : 반올림
print(round(5.1254, 2))
print(round(4.7)) #반올림되어 나타낼 소수점 자리를 표기해주지 않으면 첫째자리에서 반올림
print()

#sotred : 반복가능한 객체(interable) 정렬 후 반환
print(sorted([1,7,5,3,9,2]))
a = sorted([1,7,5,3,9,2])
print(a)
print(sorted(['p','y','t','h','o','n']))
print()

#sum : 반복가능한 객체(interable) 합 반환
print(sum([1,4,6,8,9,3]))
print(sum(range(1, 101)))
print(sum(range(1,10,2)))
print()

#type : 자료형 반환
print(type(3))
print(type([1,2,3]))
print(type({1,2,3}))
print(type((1,2,3)))
print(type('python'))
print(type({'name' : 'kim'}))
print()

#zip : 반복가능한 객체(interable)의 요소를 짝을 맞춰 tuple로 묶어서 반환
print(list(zip([10,20,30], [40,50,60])))
print(list(zip([10,20,30], [40,50]))) #짝이 맞지 않으면 맞는 것끼리만 반환
print(type(list(zip([10,20,30], [40,50,60]))[0]))
