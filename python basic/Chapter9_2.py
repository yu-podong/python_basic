# Chapter 9-2
# CSV 파일 읽기 및 쓰기
# CSV : MEMETYPE = text/csv

import csv

# EX 1
with open('./resource/test1.csv', 'r') as f:
    reader = csv.reader(f) #CSV 패키지를 읽을 떄 reader로 연
    #a = next(reader)    #Header Skip <-커서 이용
    #객체 확인
    print(reader)
    #타입 확인
    print(type(reader))
    #속성 확인
    print(dir(reader)) #__iter__ ->for문 사용 가능
    print()
    for c in reader:
        #print(c)    #csv파일의 헤더부분까지 출력 -> 리스트로 출력
        #print(type(c))
        #list to str
        print(' : '.join(c)) #-c의 리스트의 요소를 구분자로 구분

# EX 2
with open('./resource/test2.csv', 'r') as f:
    reader = csv.reader(f, delimiter = '|') #잘못된 구분자를 사용 -> 하나의 원소로 가져옴

    for c in reader:
        print(c)

# EX 3
with open('./resource/test1.csv', 'r') as f:
    reader = csv.DictReader(f) #csv파일을 딕셔너리로 가져옴
    #확인
    print(reader)
    print(type(reader))
    print(dir(reader))
    print()

    for c in reader:
        for k,v in c.items():
            print(k,v)
        print('---------------------')

# EX 4
w = [[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15],[16,17,18],[19,20,21]]

with open('./resource/write1.csv', 'w', encoding = 'UTF-8') as f:
    print(dir(csv))
    wt = csv.writer(f) #파일과 연동되서 쓰기 직전에 준비상태

    #dir 확인
    #print(dir(wt))
    #타입 확인
    #print(type(wt))

    for v in w:
        wt.writerow(v)

    #print write1.csv
with open('./resource/write1.csv','r') as f:
    read2 = csv.reader(f)

    for v in read2:
        print(' : '.join(v))

# EX 5
with open('./resource/write2.csv', 'w', encoding = 'UTF-8') as f:
    #필드명
    fields = ['One','Two','Three']
    #DictWriter
    wt = csv.DictWriter(f, fieldnames = fields) #fieldnames라는 인수 지정 -> 필드명 작성 가능
    #Header Writer
    wt.writeheader()#헤더 이름이 내부적으로 작성된 상태

    for v in w:
        wt.writerow({'One' : v[0], 'Two' : v[1], 'Three' : v[2]})
