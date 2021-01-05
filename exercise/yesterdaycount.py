file = open('yesterday.txt', 'r')

# file 객체에서 문자열을 읽은 후 변수에 저장
yesterday = file.read()

# 변수 출력
print(yesterday)
line = '-' * 100 + '\n'
print("'YESTERDAY' 개수 =", yesterday.count('YESTERDAY'))
print("'yesterday' 개수 =", yesterday.count('yesterday'))
print("'Yesterday' 개수 =", yesterday.count('Yesterday'))
print(line)

print(f'대문자로 변환 = {yesterday.upper()}')
result1 = yesterday.upper()
print("'YESTERDAY' 개수 =", result1.count('YESTERDAY'))
print(line)
print(f'소문자로 변환 = {yesterday.lower()}')
result2 = yesterday.lower()
print("'yesterday' 개수 =", result2.count('yesterday'))
print(line)
print(f'첫글자 대문자로 변환 = {yesterday.title()}')
result3 = yesterday.title()
print("'Yesterday' 개수 =", result3.count('Yesterday'))

# file 객체 닫기
file.close()