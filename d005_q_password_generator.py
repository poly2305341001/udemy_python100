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

chosen_num = []
chosen_sym = []
chosen_let = []

for num in range(0,ct_numbers):
    chosen_num.append(random.choice(numbers))                       
for sym in range(0,ct_symbols):
    chosen_sym.append(random.choice(symbols))
for let in range(0,ct_letters - ct_numbers - ct_symbols):
    chosen_let.append(random.choice(letters))

chosen_list = [chosen_let, chosen_num, chosen_sym]     
pw_list = []

for sublist in chosen_list:         # 중첩리스트를 단일의 리스트로 만들고 싶었음
    pw_list.extend(sublist)
random.shuffle(pw_list)         # 섞어섞어

pw =''.join(pw_list)    # 리스트의 요소들을 나열해서 ''로 구분된 문자열로 만들어줌 
print('생성된 비밀번호: '+ pw)