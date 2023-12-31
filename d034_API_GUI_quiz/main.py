from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface

import googletrans
# pip install googletrans==3.1.0a0

trans = googletrans.Translator()

question_bank = []
for question in question_data:
    question_text_en = question["question"]
    # print(question_text_en)
    question_text_ko = trans.translate(question_text_en, dest='ko')
    question_text = question_text_ko.text
    # question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)

# while quiz.still_has_questions():
#     quiz.next_question()

# print("You've completed the quiz")
# print(f"Your final score was: {quiz.score}/{quiz.question_number}")
