# 비밀번호 생성기
# 문자 몇개?
# 기호 몇개?
# 숫자 몇개?
# 생성된 비번:

import random
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
           'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!', '#', '$', '%', '&', '(', ')','*', '+']

print('안전한 비번 생성기')
ct_letters = int(input('몇글자 짜리?\n '))
ct_symbols = int(input(f'기호는 몇개?\n '))
ct_numbers = int(input(f'숫자는 몇개?\n '))

# for문, list, random 활용 비번 생성쓰

# random.choice 리스트의 원소를 무작위로 골라 다른 리스트에 넣기
pw_list = [0]*ct_letters

for num in range(0,ct_numbers):
    pw_list[num] = random.choice(numbers)

for sym in range(ct_numbers, ct_numbers+ct_symbols):
    pw_list[sym] = random.choice(symbols)

for let in range(ct_numbers+ct_symbols, ct_letters):
    pw_list[let] = random.choice(letters)

random.shuffle(pw_list)

for pw in pw_list:
    print(pw, end='')

# 안전한 비번 생성기
# 몇글자 짜리?
#  12
# 기호는 몇개?
#  2
# 숫자는 몇개?
#  3
# Amu&Lj96)l2B