# Chapter 9-1
#파일 읽기 및 쓰기

#읽기 모드 : r, 쓰기 모드 : w, 추가 모드 : a, 텍스츠 모드 : t(기본값), 바이너리 모드 : b
#상대경로 : ('../, ./'), 절대경로('C:\Django\example..')

#파일 읽기
# EX 1
f = open('./resource/it_news.txt', 'r', encoding = 'UTF-8') #세 번쨰 인자에서 가져올 파일이 사용한 인코딩을 작성
#속성 확인
print(dir(f))
#인코딩 확인
print(f.encoding)
#파일 이름
print(f.name)
#모드 확인
print(f.mode)

cts = f.read()
print(cts)
#반드시 close
f.close()

# EX 2
with open('./resource/it_news.txt', 'r', encoding = 'UTF-8') as f: #with문으로 파일 호츨 및 사용하면 with문이 끝날 때 자동으로 파일이 닫힘
    c = f.read()
    print(c)
    print(iter(c))
    print(list(c))
    #f.close() 사용하지 않아도 됨
print()

# EX 3
#read() : 전체 읽기, read(10) : 10byte만큼 읽어오기
with open('./resource/it_news.txt', 'r', encoding = 'UTF-8') as f: #with문으로 파일 호츨 및 사용하면 with문이 끝날 때 자동으로 파일이 닫힘
    c = f.read(20)
    print(c)
    c = f.read(20)
    print(c)    #전의 statement에서 읽었던 부분 다음부터 출력 == 커서 존재
    c = f.read(20)
    print(c)    #커서 : 파일 내용 중 마지막에 어디까지 읽었는지 내부적으로 기억
    f.seek(0,0) #seek: 탐색 -> seek(0,0) : 0,0으로 이동하고 다시 읽겠다
    c = f.read(20)
    print(c)
print()

# EX 4
#readline : 한 줄 씩 읽기 (개행이 되기 전까지)
with open('./resource/it_news.txt', 'r', encoding = 'UTF-8') as f:
    line = f.readline()
    print(line)
    line = f.readline()
    print(line)
print()

# EX 5
#readlines : 전체를 읽은 후 라인 단위로 리스트에 저장
with open('./resource/it_news.txt', 'r', encoding = 'UTF-8') as f:
    cts = f.readlines()
    print(cts)
    print()
    for c in cts:
        print(c, end = '')
print()

#파일 쓰기(write)
#우리가 쓰고자 하는 없는 파일을 가상으로 연결을 할 때도 open함수 사용
# EX 1
with open('./resource/contents1.txt', 'w', encoding = 'UTF-8') as f:
    f.write("I love python\n")

# EX 2
with open('./resource/contents1.txt', 'a', encoding = 'UTF-8') as f:
    f.write("I love python2\n") #append모드 사용 -> 기존에 작성했던 내용 다음에 write

# EX 3
#writelines : 리스트 -> 파일
with open('./resource/contents2.txt', 'w', encoding = 'UTF-8') as f:
    list = ['Orange\n', 'Apple\n', 'Banana\n', 'Melon\n']
    f.writelines(list)

# EX 4
with open('./resource/contents3.txt', 'w', encoding = 'UTF-8') as f:
    print('Test Text Write!', file = f) #print에서 file 옵션을 사용하면 콘솔창이 아닌 연결시킨 파일에 출력
    print('Test Text Write!', file = f)
    print('Test Text Write!', file = f)
