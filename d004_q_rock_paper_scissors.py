import random

# 가위바위보 게임

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
img_hands = [rock, paper, scissors]

my_choice = int(input("무엇을 내겠습니까? 바위(0), 보(1), 가위(2)"))
if my_choice >=3 or my_choice < 0:
    print("잘못된 숫자를 입력했습니다")
    # 아예 다른 숫자를 입력했을 경우
else:
    print(f"나의 선택은: {img_hands[my_choice]}")
    
    computer_choice = random.randint(0, 2)
    print(f"컴퓨터의 선택은: {img_hands[computer_choice]}")

# 바위(0) > 가위(2) , 바위(0) = 바위(0) , 바위(0) < 보(1) -- 예외처리 0 > 2
# 보(1) > 바위(0) , 보(1) = 보(1), 보(1) < 가위(2)
# 가위(2) > 보(1), 가위(2) = 가위(2), 가위(2) < 바위(0) -- 예외처리 2 < 0
    if computer_choice == 0 and my_choice == 2:
        print("컴퓨터가 이겼다")
    elif my_choice == 0 and computer_choice == 2:
        print("내가 이겼다!")
    elif computer_choice > my_choice:
        print("컴퓨터가 이겼다")
    elif my_choice == computer_choice:
        print("비겼다!")
    elif my_choice > computer_choice:
        print("내가 이겼다!")

# 무엇을 내겠습니까? 바위(0), 보(1), 가위(2)2
# 나의 선택은:
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)

# 컴퓨터의 선택은:
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)

# 비겼다!