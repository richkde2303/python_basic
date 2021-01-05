id = ['id', '1', '2', '3', '4']
name = ['name', 'hong kildong', 'lee soonsin', 'jang youngsil', 'king sejong']
email = ['email', 'hong@mail.com', 'lee@mail.com', 'jang@mail.com', 'king@mail.com']
hp_num = ['hp_num', '010-2343-9870','010-3333-5555','010-7777-1234','010-4567-0987']
print(zip(id, name, email, hp_num))
for id, name, email, hp_num in zip(id, name, email, hp_num):
    print(id, name, email, hp_num)
