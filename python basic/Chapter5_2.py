#Chapter 5-2
#파이선 사용자 입력
#Input 사용법
#기본 타입 == str

# EX 1
"""
name = input('Enter Your Name : ')
grade = input('Enter Your Grade : ')
company = input("Enter Your Company name : ")

print(name, grade, company)
"""
# EX 2
"""
number = input("Enter number : ")
name= input('Enter name : ')

print('type of number : ', type(number))
print('type of name : ', type(name))
"""

# Ex 3(계산)
"""
first_number = int(input('Enter number : '))
second_number = int(input('Enter number : '))

total = first_number + second_number
print("first_number + second_number :", total)
"""
# Ex 4
"""
float_number = float(input('Enter a float number : '))

print('input float :', float_number)
print('input type :', type(float_number))
"""

# EX 5(print문에서 input 받기)
"""print('First Name : {0}, Last Name : {1}'.format(input('Enter first name: '), input('Enter last name : ')))"""

#숫자를 공백을 기준으로 입력 받기
x, y, z = map(int, input().split())
print(x, y, z, '\n')

#숫자를 공백을 기준으로 하여 리스트 형태로 입력받기
num1 = list(map(int, input().split()))
print(num1, '\n')

#문자열을 리스트 형태로 입력받기
str1 = list(map(str, input()))
print(str1, '\n')

#문자열을 공백을 기준으로 하여 리스트 형태로 입력받기
str2 = list(map(str, input().split()))
print(str2,'\n')
