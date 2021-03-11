#Chapter 7-1
#파이썬 예외처리의 이해
#예외 종류
'''
SyntaxError : 문법이 틀렸을 경우
TypeError : 자료형에 맞지 않는 연상늘 수행할 경우
NameError : 없는 변수를 참조할 때
IndexError : 잘못된 인덱스 번호를 접근할 때
ValueError
KeyError
'''
#문법적으로는 예외가 없지만, 코드 실행 프로세스(단계)에서 발생하는 예외도 중요
# 1. 예외는 반드시 처리한다.
# 2. 로크는 반드시 남긴다. (로그 : 어떤 예외가 발생했는지 기록을 남기는 것)
# 3. 예외는 던져진다. (다른 곳으로 처리를 위임할 수가 있음)
# 4. 예외 무시도 가능 but 되도록 사용X

#SyntaxError
#print('error)
#print('error'))

#NameError
# a = 10
# b = 10
# print(c)

#zeroDivisionError
# print(100/0)

#IndexError
# x = [50, 60, 70]
# print(x[1])
# print(x[5])
#print(a.pop())
#print(a.pop())
#print(a.pop())
#print(a.pop()) #빈 리스트이기 때문에 Error 발생

#KeyError
# dic = {'name' : 'Lee', 'age' : 45, 'city' : 'Busan'}
#print(dic[hobby])
#print(dic.get('hobby'))

#예외 없는 것을 가정하고 프로그램 작성 -> 런타임 예외 발생 시 예외 처리 권장

#AttributeError : 모둘, 클래스에 있는 잘못된 속성 사용 예외
import time
# print(time.time2())

#ValueError
# x = [10, 50, 90]
# x.remove(50)
# print(x)
# x.remove(200)

#FileNotFoundError
#t = open('test.txt')

#TypeError
x = [1, 2]
y = (1, 2)
z = 'test'

# print(x + y)
# print(x + z)
# print(y + z)
print(x + list(y))
print(x + list(z))
print()

#예외 처리 기본
#try : 에라가 발생할 가능성이 있는 코드 실행
#except 에러명1 : 여러개 가능
#except 에러명2 :
#else : try 블록의 에러가 없을 경우 실행
#finally : 항상 마지막에 실행

name = ['Kim', 'Lee', 'Park']

# EX 1
try : #try문 아래에서 예외가 발생할 가능성이 있는 코드를 포함
    z = 'Kim'
    x = name.index(z)
    print('{} Found it! {} in name'.format(z, x + 1))
except ValueError :
    print('Not found it! - Occurred ValueError')
else:
    print('Ok! else')
print()

# EX 2
#Exception <- 모든 에러의 상위
try :
    z = 'Cho'
    x = name.index(z)
    print('{} Found it! {} in name'.format(z, x + 1))
except Exception: #예외명을 적어주지 않으면(or Exception) 모든 에러를 잡음 but 어떤 에러가 발생했는지 알 수 없음
    print('Not found it! - Occurred ValueError')
else:
    print('Ok! else')
print()

# EX 3
try :
    z = 'Cho'
    x = name.index(z)
    print('{} Found it! {} in name'.format(z, x + 1))
except Exception as e: #alias
    print(e)    #에러 내용 출력
    print('Not found it! - Occurred ValueError')
else:   #예외가 발생하지 않았을 때만 실행
    print('Ok! else')
finally:    #예외가 발생해도 마지막에 무조건 실행
    print('OK! finally!')
    print()

# EX 4
#예외 발생 : raise
#raise 키워드로 예외 직접 발생
try:
    a = 'Park'
    if a == 'Kim':
        print('Ok! Pass!')
    else:
        raise ValueError  #예외를 직접 발생시(파이썬의 문법적 에러가 아닌 설계에 의한 에러를 잡을 때)
except ValueError:
    print('Occurred! Exception!')
else:
    print('OK! else!')
