from tkinter import *
from quiz_brain import QuizBrain
from PIL import Image
# pip install pillow
import os
import sys

THEME_COLOR = "#FFDE70"
FONT_COLOR = "#0a0a0a"

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("컴퓨터과학 OX")
        self.window.config(padx=30, pady=20, bg=THEME_COLOR)
        self.window.iconbitmap(resource_path('images/quiz.ico'))

        self.score_label = Label(text="Score: 0", fg="black", bg=THEME_COLOR, font=("Arial", 10, "bold"))
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            width = 280,
            text = "컴퓨터과학 OX",
            fill = FONT_COLOR,
            font = ("Malgun Gothic", 13)
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=20)

        # img = Image.open("images/letter-o.png")
        # resized = img.resize((100,100))
        # resized.save("images/button-o.png")
        o_image = PhotoImage(file=resource_path("images/button-o.png"))
        self.o_button = Button(image=o_image, highlightthickness=0, command=self.o_pressed, bd=0, bg=THEME_COLOR)
        self.o_button.grid(row=2, column=0, pady=10)

        # img = Image.open("images/letter-x.png")
        # resized = img.resize((100,100))
        # resized.save("images/button-x.png")
        x_image = PhotoImage(file=resource_path("images/button-x.png"))
        self.x_button = Button(image=x_image, highlightthickness=0, command=self.x_pressed, bd=0, bg=THEME_COLOR)
        self.x_button.grid(row=2, column=1, pady=10)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}/{self.quiz.question_number}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.score_label.config(text=f"Score: {self.quiz.score}/{self.quiz.question_number}")
            self.canvas.itemconfig(self.question_text, text=f"모든 문제를 풀었습니다.\n{self.quiz.question_number}문제 중 {self.quiz.score}개의 정답을 맞혔습니다!")
            self.o_button.config(state='disabled')
            self.x_button.config(state='disabled')

    def o_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def x_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="#53AD69")
        else:
            self.canvas.config(bg="#FF4855")
        self.window.after(1000, self.get_next_question)