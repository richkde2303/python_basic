print('Guess Game 시작')

import random
guess_number = random.randint(1, 100)
print(guess_number)
print('1 ~ 100 임의의 숫자를 입력하세요')
user_input = int(input())
count_number = 1
while user_input != guess_number:
     if user_input < guess_number:
        print('숫자가 너무 작습니다')
        print('1 ~ 100 임의의 숫자를 입력하세요')
        user_input = int(input())
        count_number += 1
     elif user_input > guess_number:
        print('숫자가 너무 큽니다')
        print('1 ~ 100 임의의 숫자를 입력하세요')
        user_input = int(input())
        count_number += 1
else:
    print(f'정답은 {guess_number} {count_number}번 시도 만에 성공입니다')
    print('Guess Game 종료')
