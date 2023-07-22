############DEBUGGING#####################

# # Describe Problem
# def my_function(): #함수 정의
#   for i in range(1, 21):  #19회 반복 -> 20회 반복
#     if i == 20:  #20번째에
#       print("You got it")
# my_function()

# # Reproduce the Bug
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(0, 5) # 인덱스 1~6 -> 0~5
# print(dice_imgs[dice_num])

# # Play Computer -> 1994일 경우 답없음
# year = int(input("What's your year of birth?")) #출생연도 입력, int로 변환, 변수 year에 대입
# if year > 1980 and year < 1994: #year가 1980 초과하고 1994 미만이면
#   print("You are a millenial.") #출력
# elif year >= 1994: #year가 1994 초과하면
#   print("You are a Gen Z.") #출력

# # Fix the Errors
# age = int(input("How old are you?")) #age가 문자열
# if age > 18:
#  print(f"You can drive at age {age}.") #들여쓰기 #f-string

# #Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# print(pages)
# word_per_page = int(input("Number of words per page: ")) #== ㅋㅋㅋㅋ
# print(word_per_page)
# total_words = pages * word_per_page
# print(total_words)

#Use a Debugger -> pythontutor.com
def mutate(a_list):
  b_list = []
  for item in a_list:
    new_item = item * 2
    b_list.append(new_item) #append가 미반복
  print(b_list)

mutate([1,2,3,5,8,13])