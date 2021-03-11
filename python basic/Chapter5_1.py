#Chapter 5-1
#파이선 함수 및 중요성
#파이썬 함수식 및 람다(lambda)

#함수 정의 방법
#def founction_name(parameter):
#   code

# EX 1
def first_func(w):
    print('Hello,', w,'\n')

word ="Good boy"
first_func(word)
print()

# EX 2
def return_func(w1):
    return "Hello, " + str(w1)

x = return_func('Good boy2')
print(x)
print()

# EX 3(다중 변환)
def func_mul(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return y1, y2, y3

x, y, z = func_mul(10)
print(x, y, z)
print()

#튜플 리턴
def func_mul2(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return (y1, y2, y3)

q = func_mul2(20)
print(type(q), q)
print()

#리스트 리턴
def func_mul3(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return [y1, y2, y3]

q = func_mul3(30)
print(type(q), q)
print()

#딕셔너리 리턴
def func_mul4(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return {'test1' : y1, 'test2' : y2, 'test3' :y3}

d = func_mul4(20)
print(type(d), d)
print(d, d.get('test1'), d.values(), d.keys())
print(d.items(),'\n')
#중요
# *arge, **kwarges

#*arge(언팩킹) : 가변 인수 사용
def args_func(*args): #*args : 전달되는 인수들을 하나의 튜플로 인식
    for i, v in enumerate(args): #enumerate(열거하다) : 순서가 있는 자료형을 입력받아 인데긋 값을 포함하는 객체 return
        print('Result : {} {}'.format(i, v))
    print('------------ ')

args_func('Lee')
args_func('Lee', 'Park')
args_func('Lee', 'Park', 'Kim')

#**kwargs : 딕셔너리 자료형 언팩킹
def kwargs_func(**kwargs):
    for v in kwargs.keys():
        print('{}'.format(v), kwargs[v])
    print('-----------------')

kwargs_func(name1 = 'Lee')
kwargs_func(name1 = 'Lee', name2 = 'Park')
kwargs_func(name1 = 'Lee', name2 = 'Park', name3 = 'Cho', sendSMS=True)

#전체 혼합
def example(args_1, args_2, *args, **kwargs):
    print(args_1, args_2, args, kwargs,'\n')

example(10,20, 'Lee', 'Park', 'Kim', Age1 = 20, Age2 = 30, Age3 = 40)

#중첩함수
def nested_func(num):
    def func_in_func(num):
        print(num)
    print("In func")
    func_in_func(num + 100)

nested_func(100)
print()

"""
func_in_func(100) -> ERROR 발생
    because 부모 함수를 호출하지 않고는 자식 함수는 정의되지 않기 때문
    == 자식 함수를 사용할 수 있는 시점은 부모 함수 호출 후 자식 함수 정의 부분이 실행될 때
"""

#lambda 예제
#메모리 절약, 가독성 향상, 코드 간결
#함수는 객체 생성 -> 리소스(메모리) 할당
#람다는 즉시 실행 함수(heap 초기화) -> 메모리 초기화
#남발 시 가독성 오히려 감소

#일반적 함수 -> 할당
def mul_func(x,y):
    return x * y
print(mul_func(10 ,50),'\n')

#람다 함수 -> 할당
lmabda_mul_func = lambda x, y: x * y #ladbda식 : 이름X, 변수에 담아서 사용 or 함수 인수로 넘길 수 있음
print(lmabda_mul_func(50, 50),'\n')

def func_final(x, y, func):
    print(x * y * func(100, 100))

func_final(10 ,20, lambda x,y: x * y)

# Hint
def tot_length1(word: str, num: int) -> int:
    return len(word) * num

print('hint exam1 : ', tot_length1("i love you", 10))

def tot_length2(word: str, num: int) -> None:
    print('hint exam2 : ', len(word) * num)

tot_length2("niceman", 10)
