#Chapter 2-1
#파이썬 완전 기초
#Print 사용법

#기본 출력
print("Python Start!")  #대체로 많이 쓰임
print('Python Start!')  #대체로 많이 쓰임
print('''Python Start!''')
print("""Python Start!""")

print() #이스케이프 문자도 있음

#separator 옵션
print('P','Y','T','H','O','N')  # , : 문자열 띄어쓰기
print('P','Y','T','H','O','N', sep='')
print('P','Y','T','H','O','N', sep=',')
print('P','Y','T','H','O','N', sep='|')
print('P','Y','T','H','O','N', sep='    ')
print('010','1111','2222',sep='-')
print('python','google.com', sep='@')

print()

#end 옵션
print('Welcome to', end=' ') #end 옵션에 들어간 문자로 다음 print문을 이어줌
print('IT News', end=' ')    #print문을 옵션 없이 사용 시 자동으로 줄바꿈 가능
print('Web Site')
print()

#file 옵션
import sys #import는 예약어
print('Learn Python',file=sys.stdout) #print문의 내용을 지정한 파일에 저장(stdout=콘솔 아웃 의미)
print()

#format 사용 (d : 정수 , s : 문자열, f : 실수), 기본적으로 숫자는 오른쪽, 문자열은 왼쪽 정렬
print('%s %s' %('one', 'two'))
print('{} {}'.format('one','two'))  #암묵적으로 {0} {1}
print('{1} {0}'.format('one','two'))    #format함수안의 첫번째 문자열을 {0}인 곳으로 출력 becuase 컴퓨터는 0부터 시작

print()

#%s
print('%10s' %('nice')) #%10s는 총 10개의 자릿수 의미
print('{:>10}'.format('nice')) #> : 왼쪽

print('%-10s' %('nice'))    #+ : 왼쪽부터 공백 채움, - : 오른쪽부터 공백 채움
print('{:10}'.format('nice')) #오른쪽부터 공백 채움

print('{:_>10}'.format('nice')) #원하는 기호로 부족한 자릿수 채움
print('{:^10}'.format('nice'))  #문자열을 중앙 정렬

print('%.5s' %('nice'))
print('%5s' %('pythonstudy'))   #자릿수를 지정했지만 입력한 문자열 모두 출력 가능
print('%.5s' %('pythonstudy'))  #지정한 자릿수만큼 문자열을 절삭
print('{:10.5}'.format('pythonstudy')) #공간은 10개 출력되는 자릿수 5개

print()

#%d
print('%d %d' %(1, 2))
print('{} {}'.format(1, 2))

print('%4d' %(42))
print('{:4d}'.format(42)) #정수형일 경우 d를 붙여줘야 함

print()

#%f
print('%f' %(3.14134234234324))
print('%1.8f' %(3.14234324343)) #정수부 - 1자리, 소수부 - 8자리 출력
print('{:f}'.format(3.14134234234324))
print('%06.2f' % (3.14159265358943))    #총 6자리 중 정수부는 하나이기에 나머지 부분을 0으로 채움 >>소수부 2자리 출력
print('{:06.2f}'.format(3.14159265358943))

print()
