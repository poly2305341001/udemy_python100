from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from restore import Restore

restore = Restore()

question_bank = []
for q in question_data:
    # question = Question(q["text"], q["answer"])

    q_text = q["question"]      # 문자열은 오타가 나기 쉽기 때문에 객체로 바꿔주고 작업하는 게 좋다네?
    q_restore = restore.all_quot(q_text)        # 이건 걍 특문 깨진 거 고쳐보고 싶어서 넣어봄
    q_answer = q["correct_answer"]      # 그러면 실수할 확률이 적어진대 왜냐면 객체는 오타가 나면 파이참에서 표시를 해주고 자동완성도 쓸 수 있으니까
    question = Question(q_restore, q_answer)
    # question_bank += question     # 여긴 또 이게 안 되네 Question 객체는 순회가 안 된대 -> +=는 리스트끼리 더하는 거래! 와 이제 알았다
    question_bank.append(question)      # question_bank리스트의 원소들은 다 Questino()객체임

quiz_brain = QuizBrain(question_bank)

while quiz_brain.still_has_questions():
    choice = quiz_brain.next_question()

# quiz_brain.end_of_game()

print("You've completed the quiz.")
print(f"Your final score was: {quiz_brain.score}/{quiz_brain.question_number}")
