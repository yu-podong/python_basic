#Chapter 3-2
#파이썬 문자형
#문자형 중요

#문자열 생성
str1 = "I am Python"
str2 = 'Python'
str3 = """How are you?"""
str4 = '''Thank you!'''

print(type(str1), type(str2), type(str3), type(str4))
print(len(str1), len(str2), len(str3), len(str4)) # len함수 == strlen 함수

#빈 문자열
str1_t1 = ''
str2_t2 = str()

print(type(str1_t1), len(str1_t1))
print(type(str2_t2), len(str2_t2))

#이스케이프 문자 사용
"""
참고 : Escape 코드

\n : 개행
\t : 탭
\\ : 문자
\' : 문자
\" : 문자
\000 : 널 문자
"""
#I'm boy

print("I'm boy") #작은 따옴표는 I'm boy로 출력 X
print('I\'m Boy')
print('a \t b')
print('a \n b')
print('a \"\" b')

escape_str1 = "Do you have a \"retro games\"?"
print(escape_str1)
escape_str2 = 'What\'s on TV?'
print(escape_str2)

#탭, 줄 바꿈
t_s1 = "Click \t Start!"
t_s2 = "New Line \n Check!"

print(t_s1)
print(t_s2)
print()

#Raw String : 역 슬래쉬 신경 X, 드라이브 경로를 가지고 파일 복사 시 사용, 문자열 앞에 r 사용
raw_s1 = r'D:\python\test'
print(raw_s1)

#멀티라인 입력
# \ : 역슬래쉬로 끝나면 이 다음 어떤 변수를 바인딩을 한다고 인식
multi_str = \
'''
String
Multi line
Test
'''

multi_str2 = '''
String
Multi line
Test
'''

multi_str3 = \
'String\n' \
'Multi line\n' \
'Test'

print(multi_str)
print(multi_str2)
print(multi_str3)
print()

#문자열 연산
#시퀀스 형태인 데이터 타입은 'in 연산자' 사용 가능
str_o1 = "python"
str_o2 = "Apple"
str_o3 = "How are tou doing"
str_o4 = "Seoul Deajeon Busan Jinju"

print(str_o1 * 3)
print(str_o1 + str_o2)
print('y' in str_o1) #str_o1안에 y라는 문자가 포함되어 있니?
print('z' in str_o1)
print('P' not in str_o2) #대소문자 구분
print()

#문자열 형 변환
print(str(66), type(str(66)))
print(str(10.1), type(str(10.1)))
print(str(True), type(str(True)))
print()

#문자열 함수(upper, isalnum, startswith, count, endswith, isalpha...)
print("Capitalize : ", str_o1.capitalize())
print("endswith : ", str_o2.endswith("e")) #마지막 문자가 무엇인지 알아보는 함수
print("replace : ", str_o1.replace("thon", ' Good')) #지정된 문자열 안에서 첫번째 문자열에 해당하는 부분을 두번째 문자열로 Change
print("sorted : ", sorted(str_o1))
print("join str: ", str_o1.join(["I'm ", "!"]))
print("split: ", str_o4.split(' ')) #split 함수 안의 구분자로 문자열 분리 후 리스트 형태로
print("reversed1: ", reversed(str_o2)) #list 형 변환
print("reversed2: ", list(reversed(str_o2)))
print()

#반복 (시퀀스) : 슬라이싱 처리 가능
im_str = "Good Boy"
print(dir(im_str)) #__iter__ : 반복을 할 수 있다는 의미 , dir함수를 통해  im_str에서 사용 가능한 속성을 나열

#출력
for i in im_str :
    print(i)
print()

#슬라이싱 연습
str_s1 = "Nice Python"
print(len(str_s1))

print(str_s1[0:3])  #0 1 2까지만 print (항상 3-1번째 까지만) ==인덱스처럼 생각
print(str_s1[5:11]) #5 6 7 8 9 10 == print(str_s1[5:])
print(str_s1[:len(str_s1)]) # str_s1[:11] == str_s1[:]
print(str_s1[1:4:2]) # 3번째 인수 : 단위 -> 1번째부터 3번째까지 출력하되 2칸 씩 건너뛰어 출
print(str_s1[-5:]) #음수일 경우 : 오른쪽에서 -1부터 시작
print(str_s1[1:-2]) #-3까지
print(str_s1[::2])
print(str_s1[::-1])

#아스키 코드(or 유니코드)
a = 'z'
print(ord(a)) #ord : 문자의 아스키 코드 값 출력
print(chr(122)) #chr : 아스키 코드에 해당하는 문자 출력
