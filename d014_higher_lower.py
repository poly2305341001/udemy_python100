from d014_art import logo
from d014_game_data import data
import random

# 중복없이 뽑기 함수
def randomchoice():
    # 예외처리(데이터 동났을 때)
    if len(left_data) == 0:
        print("You've compared all data. You win perfectly!")
        return 0
    else:
        chosen = random.choice(left_data)
        left_data.remove(chosen) #이게 함수 안에서 유효한지 모르겠네 흠 -> 매우 유효하구만
        return chosen

# 게임 시작
while 1:
    game_over = False

    # 로고 출력
    print(logo)

    # 시작 점수는 0점
    score = 0

    # 원본 데이터 살려두고 이미 쓴 패는 제거하도록 사본 만들어 둠
    left_data = data.copy()

    # 중복없이 데이터 2개 뽑자 -> 함수화 ㄱㄱ
    compare_A = randomchoice()
    compare_B = randomchoice()

    while game_over == False:
        # 팔로워 비교해서 더 많은 애를 답으로 설정해놔야지
        right_answer = compare_A
        if compare_A['follower_count'] < compare_B['follower_count']: 
            right_answer = compare_B

        # 두 데이터 정보 줘야지
        print(f"Compare A: {compare_A['name']}, a(an) {compare_A['description']}, from {compare_A['country']}")
        print("vs.")
        print(f"Compare B: {compare_B['name']}, a(an) {compare_B['description']}, from {compare_B['country']}")

        # 유저야 선택해라
        user_choice = input("\nWho has more followers? Type 'A' or 'B': ").upper()
        if user_choice == 'A':
            user_choice = compare_A
        elif user_choice == 'B':
            user_choice = compare_B

        # 유저 답이랑 비교하고 맞으면 1점 더해주고 다음 단계
        if user_choice == right_answer:
            score += 1
            print(f"You're right! Current score: {score}.\nKeep going.\n")

            # 팔로워 더 많은 애를 A로 옮기고 새로운 데이터 데려 와서 B에 넣어
            compare_A = right_answer
            compare_B = randomchoice()

            # 다시 비교하고 무한 반복
            # 비교할 거 안 남았으면 게임 종료
            if compare_B == 0:
                game_over = True

        # 틀리면 game over
        else :
            print(f"That's wrong! GAME OVER")
            game_over = True
    
    # 게임 끝났을 때 다시 할래?
    print(f"Final score: {score}.\n")
    retry = input("If you want to try again, type 'r': ").lower()
    if retry == 'r':
        continue
    else:
        break