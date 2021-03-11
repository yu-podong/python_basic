#Chapter 2-2
#파이썬 완전 기초
#파이썬 변수

#기본 선언
n = 700

#출력
print(n)
print(type(n)) #변수의 자료형을 출력

#동시 선언
x = y = z = 700
print(x, y, z)

#선언
var = 75

#재선언
var = "Change Value"

#출력
print(var)
print(type(var))

#Object References
#변수 값 할당 상태
#1. 타입에 맞는 오브젝트 생성
#2. 값 생성
#3. 콘솔 출력

#ex 1)
print(300)
print(int(300))

#ex 2)
#n -> 777
n = 777

print(n, type(n))

m = n #m -> 777 <- n

print(m, n)
print(type(m),type(n))
print()

m = 444
print(m, n)
print(type(m),type(n))
print()

#id(identity) 확인 : 객체의 고유값 확인
m = 800
n = 655

print(id(m))
print(id(n))
print(id(m) == id(n))
print()

#같은 오브젝트 참조
m = 800
n = 800

print(id(m))
print(id(n))
print(id(m) == id(n)) #여러 변수에 같은 값으로 초기화하면 하나의 오브젝트만 생성(id값 same)
print()

#다양한 변수 선언
#Comel Case : numberOfCollegeGraduates -> Method
#Pascal Case : NumverOfCollegeGraduates -> Class
#Snake Case : number_of_college_graduates -> 변수

#허용하는 변수 선언 법
age = 1
Age = 2
aGe = 3
AGE = 4
a_g_e = 5
_age = 6
age_ = 7
_AGE_ = 8
'''1AGE = 9 >>숫자로 시작하는 변수 선언 불가능'''

#예약어는 변수명으로 불가능(python reserved word 검색 자료 참조)
"""
False   def    if   raise
None    del   import   return
True   elif   in   try
and else   is   while
as   except   lambda   with
assert   finally   nonlocal   yield
break   for   not
class   from   or
continue   global   pass
"""
