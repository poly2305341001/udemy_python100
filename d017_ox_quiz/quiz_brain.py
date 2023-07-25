class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        # 제일 마지막 단계에 추가함
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)       # next_question()에서 += 1 된 건 고려 안 해도 됨 어차피 그건 문제 나올 때 적용되는 거니까! 그래서 <= 아니고 <임
        #     return True       # 이딴 것도 필요없네
        # else:     #  애초에 비교식이니까 바로 True False 튀어나오잖음 ㄷㄷ
        #     return False

    def next_question(self):
        q = self.question_list[self.question_number]
        # 여기서 quistion_list는 main.py에서 question_bank임
        # 그리고 quesition_bank의 원소들은 다 Question()객체임
        # 즉 text와 answer라는 속성을 가진 거고 그래서 q 역시 그런 속성들을 가짐 점연산자 쓸 수 있단 얘기
        # 그치만 여기서 점연산자 써도 자동완성은 안 될 거임 왜냐하면 Question()은 다른 모듈에 있거든! 걍 이 구조를 이해하고 내가 쓸 걸 쓰면 프로그램이 돌아가면서 링크될 거임! 아 대박
        self.question_number += 1
        # input(f"Q.{self.question_number}: {q.text} (T/F)?: ").upper()
        # 제일 마지막 단계에 추가함
        user_answer = input(f"Q.{self.question_number}: {q.text} (T/F)?: ").upper()
        self.check_answer(user_answer, q.answer)
        # if answer == "T":     # 이딴건 노 필요
        #     return True       # 이런 것까지 다 분리
        # elif answer == "F":   # 모듈화란 이런 거구나... ㄷㄷ
        #     return False      # 위의 check_a~()로 이동쓰

    def check_answer(self, user_answer, correct_answer):
        if user_answer.upper() == correct_answer[0].upper():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong...")
            print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}\n")
    #
    # def end_of_game(self):
    #     print("You've completed the quiz.")
    #     print(f"Your final score was: {self.score}/{self.question_number}")