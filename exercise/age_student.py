from datetime import datetime as dt

print('태어난 년도를 입력하세요 : ')
student_birth = int(input())
current_year = dt.today().year
print(dt.today())
print(current_year)

age = current_year - student_birth + 1
print('나이는 : ', age)

if 15 <= age < 20:
    print('고등학생')
elif 20 <= age <= 28:
    print('대학생')
else:
    print('학생이 아닙니다')
