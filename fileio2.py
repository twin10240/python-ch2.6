# 다양한 파일 입출력 함수

f = open('test.txt', 'r', encoding='utf-8')
text = f.read()
print(text)

pos = f.tell()
print(pos)

f.seek(12)
print(f.tell())
text = f.read()
print(text)
f.close()

f = open('fileio2.py', 'r', encoding='utf-8')
while True:
    line = f.readline()
    if line == '':
        f.close()
        break

    print(line, end='')

f = open('fileio2.py', 'r', encoding='utf-8')
lines = f.readlines()
for line in lines:
    print(line, end='')

f.close()

# with ~ as (자원정리)
with open('fileio2.py', 'r', encoding='utf-8') as f2:
    lines = f2.readlines()
    for line in lines:
        print(line, end='')

print(f2.cl)
