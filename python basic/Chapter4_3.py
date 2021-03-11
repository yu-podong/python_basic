#Chapter 4-3
#파이썬 반복문
#While 실습

#while <expression>:
#   <statement(s)>

# EX 1
n = 5

while n > 0:
    print(n)
    n -= 1
print()

# EX 2
a = ['foo', 'bar', 'baz']

while a:
    print(a.pop(-1)) #a.pop(0) -> 'foo'부터 출력
print()

# EX 3
#break, continue
n = 5
while n > 0:
    n -= 1
    if n == 2:
        break
    print(n)
print('Loop Ended\n')

# EX 4
m = 5
while m > 0:
    m -= 1
    if m ==2:
        continue
    print(m)
print("Loop Ended\n")

# EX 5
i = 1

while i <= 10:
    print('i :', i)
    if i == 6:
        break
    i += 1
print()

# EX 6
#while - else 구문
n = 10
while n > 0:
    n -= 1
    print(n)
    if n == 5:
        break
else:
    print('else out')

# EX 7
a = ['foo', 'bar', 'baz', 'qux']
s = 'kim'
i = 0

while i < len(a):
    if a[i] == s:
        break
    i += 1
else:
    print(s, 'not found in list.\n')

#무한 반복
#while True:
#   print('Foo')

# EX 8
a = ['foo', 'bar', 'baz']

while True:
    if not a:
        break
    print(a.pop())
