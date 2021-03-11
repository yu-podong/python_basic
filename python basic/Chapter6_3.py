# Chapter 6-3
#파이썬 패키지
#파이썬 작성 및 사용법
#파이썬은 패키지로 분할된 개별적인 모듈로 구성
#상대경로 : .. (부모 디렉터리), . (현재 디렉터리) -> 모듈 내부에서만 사용
#__inti__.py : Python 3.3부터는 없어도 패키지로 인식 -> 단, 하위 호환을 위해 작성 추천, 패키지라는 것을 인식시켜주기 위한 수단
#__all__ = ['모듈 이름'] : __all__에 적혀있는 모듈을 외부에서 import를 할  허가해주는 역할
#__all__에 적혀있지 않으면 외부에서 사용 불가 -> 파이썬은 init 파일을 먼저 검사하기 떄문

# EX 1
import sub.sub1.module1 #같은 디렉터리(python basic)에 있는 패키지를 import를 통해 호출 가능
import sub.sub2.module2 #현재 Chapter6_3이 포함되어 있는 python basic의 부모 디렉터리는 바탕화면

#사용
sub.sub1.module1.mod1_test1() #module1 파일의 경로를 출력하는 메소드(inspect함수 이용)
sub.sub1.module1.mod1_test2()
print()

sub.sub2.module2.mod2_test1()
sub.sub2.module2.mod2_test2()
print()

# EX 2
from sub.sub1 import module1
from sub.sub2 import module2 as m2  #alias

module1.mod1_test1()
module1.mod1_test2()

m2.mod2_test1()
m2.mod2_test2()
print()

# EX 3
from sub.sub1 import * #* : sub1 패키지에 있는 모든 모듈을 가져옴, 모든 하위에 있는 모든 파일의 이름으로 접근 가능
from sub.sub2 import *

module1.mod1_test1()
module1.mod1_test2()

module2.mod2_test1()
module2.mod2_test2()
print()

# EX 4
'''
import sub.sub3.package_test
print(sub.sub3.package_test.add(10, 2))
'''

from sub.sub3 import package_test as test

print(test.add(10, 10))
print(test.subtract(10, 2))
print(test.multiply(5, 2))
print(test.divide(50, 10))
