#Chapter 6-1
#파이썬 클래스
#OOP(객체 지향 프로그래밍), Self, 인스턴스 메소드, 인스턴스 변수

#클래스 and 인스턴스(== 클래스로 만든 객체) 차이 이해
"""
#객체와 인스턴스의 차이
ex) a = Cookie()
a는 객체, a는 Cookie의 인스턴스
-> 인스턴스 : 특정 객체가 어떤 클래스의 객체인지를 관계 위주로 설명할 때 사용
"""
#객체 : 클래스로 만든 피조물
#클래스 변수 : 직접 접근 가능, 공유
#인스턴스 변수 : 객체마다 별도 존재
#메소드 : 클래스 안에 구현된 함수

# EX 1
class Dog(object): #object를 상속받을 수 있음
    #클래스 속성
    species =  'firstdog'   #클래스 변수

    #모든 클래스는 초기화 메소드를 가짐 == 생성자 -> 객체가 생성될 떄 자동으로 호출되는 메서드
    #초기화/인스턴스 속성
    def __init__(self, name, age):
        self.name = name
        self.age = age

#클래스 정보
print(Dog)

#인스턴스화
a = Dog("mikky", 2)
b = Dog('baby', 3)
c = Dog("mikky", 2)

#비교
print(a == b, id(a), id(b), id(c)) #서로 다른 객체 변수는 독립적인 값 유지

#네임스페이스 : 객체를 인스턴스화 할 떄 저장된 자기만의 공간
print('dog1', a.__dict__)
print('dog2', b.__dict__)

#인스턴스 속성 확인
print('{} is {} and {} is {}\n'.format(a.name, a.age, b.name, b.age))

if a.species == 'firstdog':
    print('{0} is a {1}\n'.format(a.name, a.species))

print(Dog.species)
print(a.species)
print(b.species)

# EX 2
#Self의 이해
class SelfTest:
    def func1():
        print('Func1 called','\n')
    def func2(self): #self는 인스턴스 요구
        print(id(self))
        print('Func2 called','\n')

f = SelfTest()
print(dir(f))
print(id(f),'\n')

#f.func1()  #예외
SelfTest.func1()  #self가 없기 때문에 클래스로 바로 접근(인스턴스 필요X)

f.func2()
SelfTest.func2(f)

# Ex 3
#클래스 변수, 인스턴스 변수
class Warehouse:
    #클래스 변수(클래스 내의 모든 메소드에서 공유)
    stock_num = 0 #재고

    def __init__(self, name):
        #인스턴스 변수
        self.name = name
        Warehouse.stock_num += 1

    def __del__(self):  #객체가 소멸할 떄 자동으로 호출되는 함수
        Warehouse.stock_num -= 1

user1 = Warehouse('Lee')    #인스턴스화
user2 = Warehouse('Cho')

print(Warehouse.stock_num)
"""Warehouse.stock_num = 50 #직접 접근으로 값 수정 가능"""
print(user1.name)
print(user2.name)
print(user1.__dict__)
print(user2.__dict__)
print('before', Warehouse.__dict__)
print(user1.stock_num)  #인스턴스 __dict__에는 없지만 Warehouse의 네임스페이스에 찾아가서 stock_num 출력

del user1
print('after', Warehouse.__dict__)

# EX 4
class Dog2(object):
    species =  'firstdog'   #클래스 변수

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        return '{} is {} years old'.format(self.name, self.age)

    def speak(self, sound):
        return '{} says {}!'.format(self.name, sound)

#인스턴스 생성
c = Dog2('july', 4)
d = Dog2('marry', 10)

#메소드 호출
print(c.info())
print(d.info(),'\n')

print(c.speak('Wal Wal'))
print(d.speak('Mung Mung'),'\n')

# EX 5
#클래스 상속 : 어떤 클래스를 만들 때 다른 클래스의 기능을 물려받을 수 있게 만드는 것
class FourCal:
     def __init__(self, first, second):
         self.first = first
         self.second = second
     def add(self):
         result = self.first + self.second
         return result
     def div(self):
         result = self.first / self.second
         return result

class MoreFourCal(FourCal): #클래스를 상속하기 위해서 콸호(object) 안에 상속할 클래스 이름 작성
    def pow(self):
        result = self.first ** self.second
        return result

a = MoreFourCal(4, 2)
print(a.add())
print(a.pow(),'\n')  #print(MoreFourCal.pow(a))
"""
기존의 클래스를 변경하지 않고 기능 추가 or 기존 기능을 변경
why 기존의 클래스를 수정하면 안되는 건가?
    because 기존 클래스가 라이브러리 형태로 제공 or 수정이 허용되지 않는 상황일수도 있음
"""

# EX 6
#매소드 오버라이딩(Overriding, 덮어쓰기) : 부모 클래스(상속한 클래스)에 있는 매서드를 동일한 이름으로 다시 만드는 것
temp = FourCal(4, 0)
'''print(temp.div()) -> ZeroDivisionError 발생 but 0으로 출력하고 싶으면?'''

class SafeFourCal(FourCal):
    def div (self):
        if self.second == 0:
            return 0
        else:
            return self.first / self.second

temp = SafeFourCal(4, 0)
print(temp.div())
