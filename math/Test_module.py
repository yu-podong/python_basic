# Chapter 6-2
#파이썬 모듈
#Module : 함수, 변수, 클래스 등 파이썬 구성 요소 등을 모아놓은 파일
# sys.path에 원하는 모듈의 경로를 등록 -> 다른 파일에서 사용 가능 == C의 include와 비슷?

def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x ,y):
    return x * y
def divide(x, y):
    return x / y
def power(x, y):
    return x ** y

print('-' * 15)
print('called inner!')
print(add(5, 5))
print(subtract(5, 5))
print(multiply(5, 5))
print(divide(5, 5))
print(power(5, 5))
print('-' * 15)
