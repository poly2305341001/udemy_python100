from tkinter import *
from quiz_brain import QuizBrain
from PIL import Image

THEME_COLOR = "#FFD93D"
FONT_COLOR = "#010101"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("컴퓨터과학 OX")
        self.window.config(padx=30, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", fg=FONT_COLOR, bg="white")
        self.score_label.grid(row=0, column=0)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            width = 280,
            text = "컴퓨터과학 OX",
            fill = FONT_COLOR,
            font = ("Malgun Gothic", 13, "italic")
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=20)

        img = Image.open("images/letter-o.png")
        resized = img.resize((100,100))
        resized.save("images/button-o.png")
        true_image = PhotoImage(file="images/button-o.png")
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.true_pressed, bd=0, bg=THEME_COLOR)
        self.true_button.grid(row=2, column=0, pady=10)

        img = Image.open("images/letter-x.png")
        resized = img.resize((100,100))
        resized.save("images/button-x.png")
        false_image = PhotoImage(file="images/button-x.png")
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.false_pressed, bd=0, bg=THEME_COLOR)
        self.false_button.grid(row=2, column=1, pady=10)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="모든 문제를 푸셨습니다.")
            self.true_button.config(state='disabled')
            self.false_button.config(state='disabled')
    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)


    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(500, self.get_next_question)