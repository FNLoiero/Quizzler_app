THEME_COLOR = "#375362"
from tkinter import *
from quiz_brain import QuizBrain

class QuizzInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.windows = Tk()
        self.windows.title("Quizz App")
        self.windows.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score = 0
        self.label_score = Label(text=f"Score: {self.score}", fg="white", bg=THEME_COLOR)
        self.label_score.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = \
            (self.canvas.create_text
             (150,125,width=280,text="golas asdjhas asidh",
              fill=THEME_COLOR,
              font= ("Arial",14,"italic")))
        self.canvas.grid(row=1, column=0, columnspan=2,pady=50)


        self.img_true = PhotoImage(file="images/true.png")
        self.true_button = Button(image=self.img_true, highlightthickness=0, command=self.asw_true)
        self.true_button.grid(row=2, column=0)

        self.img_false = PhotoImage(file="images/false.png")
        self.false_button = Button(image=self.img_false, highlightthickness=0, command=self.asw_false)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.windows.mainloop()

    def get_next_question(self):
        self.true_button.config(state="normal")
        self.false_button.config(state="normal")
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text,text=q_text)
        else:
            self.canvas.itemconfig(self.question_text,text="se termino el juego")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def asw_true(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def asw_false(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if(is_right):
            self.canvas.config(bg="green")
            self.score +=1
        else:
            self.canvas.config(bg="red")

        self.label_score.config(text=f"Score: {self.score}", fg="white", bg=THEME_COLOR)
        self.true_button.config(state="disabled")
        self.false_button.config(state="disabled")
        self.windows.after(1000,self.get_next_question)