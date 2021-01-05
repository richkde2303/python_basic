print('구구단 몇 단을 계산할까요(1-9)?')
user_input = int(input())

i = 1
if 0 < user_input < 10:
    print(f'구구단{user_input}단을 계산합니다.')
    while i < 10:
        result = user_input * i
        print(f'{user_input} * {i} = {result}')
        i += 1
else:
    print('구구단 게임을 종료합니다')