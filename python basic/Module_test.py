#모듈 사용 실습
import sys

print(sys) #built-in : 파이썬 내부적으로 쓰임 (이미 만들어진 것)
print(sys.path) #파이썬, 모듈, 패키지 등이 주로 설치된 경로를 보여줌(리스트 형태)

print(type(sys.path))

#모듈 경로 삽입
#sys.path에 영구적으로 등록하려면 환경 변수에 있는 파이썬 패스에 경로를 추가해줘야 함
sys.path.append('C:\\Users\\yu01g\\OneDrive\\바탕 화면\\math') #영구적 등록X, 이 코드 상에서만 존재
print(sys.path)

import Test_module  #해당 모듈 안의 코드의 실행 결과를 보여줌
print(Test_module) #경로 출력

#모듈 사용
print(Test_module.power(10, 3))

#모듈 호출 및 사용
import Chapter6_2
print(Chapter6_2.add(10, 2))
