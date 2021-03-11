import sys
import inspect
# from ..sub2 import module2

# module1.py
def mod1_test1():
	print ("Module1 -> Test1")
	print("Path : ", inspect.getfile(inspect.currentframe()))
	# inspect(조사하다), 현재 실행 프레임의 파일의 위치를 나타내는 메소드

def mod1_test2():
	print ("Module1 -> Test2")
	print("Path : ", inspect.getfile(inspect.currentframe()))
