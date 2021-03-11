# Chapter 6-2
#파이썬 모듈
#Module : 함수, 변수, 클래스 등 파이썬 구성 요소 등을 모아놓은 파일
#sys.path에 원하는 모듈의 경로를 등록 -> 다른 파일에서 사용 가능 == C의 include와 비슷?
#모듈들의 모임 -> 패키지
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

# print('-' * 15)
# print('called inner!')
# print(add(5, 5))
# print(subtract(5, 5))
# print(multiply(5, 5))
# print(divide(5, 5))
# print(power(5, 5))
# print('-' * 15)

#__name__사용
#__main__ : 실행되는 그 대상
if __name__ == '__main__': #실행하는 위치가 import를 이용해 호출을 한다면(내 자신을 실행한다면)
    print('-' * 15)
    print('called __main__')
    print(add(5, 5))
    print(subtract(5, 5))
    print(multiply(5, 5))
    print(divide(5, 5))
    print(power(5, 5))
    print('-' * 15)
