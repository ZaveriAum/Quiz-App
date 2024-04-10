from tkinter import *
from quiz_brain import QuizBrain
from data import question_data, options
import html
THEME_COLOR = "#375362"


class QuizInterface:

    questionNumber = -1

    def __init__(self, quiz_brain: QuizBrain):

        self.options = options
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(background=THEME_COLOR, pady=20, padx=20)

        self.score = 0
        self.score_label = Label(self.window, text=f"Score: {self.score}", foreground="white", background=THEME_COLOR)

        self.canvas = Canvas(width=600, height=500, background="white")

        self.question = self.canvas.create_text(300, 250, width=580, text="Question goes here",
                                                font=("Ariel", 20, "italic"))
        self.option_a = Button(text="A", highlightthickness=0, command=self.check_if_answer_option_a,
                               font=("Ariel", 40, "normal"))
        self.option_b = Button(text="B", highlightthickness=0, command=self.check_if_answer_option_b,
                               font=("Ariel", 40, "normal"))
        self.option_c = Button(text="C", highlightthickness=0, command=self.check_if_answer_option_c,
                               font=("Ariel", 40, "normal"))
        self.option_d = Button(text="D", highlightthickness=0, command=self.check_if_answer_option_d,
                               font=("Ariel", 40, "normal"))
        self.correct = Button(text="TRUE", highlightthickness=0, command=self.check_if_answer_true, font=("Ariel", 30))
        self.incorrect = Button(text="FALSE", highlightthickness=0, command=self.check_if_answer_false,
                                font=("Ariel", 30))

        if question_data[QuizInterface.questionNumber]['type'] == "multiple":
            self.score_label.grid(row=0, column=3)
            self.canvas.grid(row=1, column=0, columnspan=4)

            self.option_a.grid(row=2, column=0)

            self.option_b.grid(row=2, column=1)

            self.option_c.grid(row=2, column=2)

            self.option_d.grid(row=2, column=3)

        else:
            self.score_label.grid(row=0, column=1)
            self.canvas.grid(row=1, column=0, columnspan=2)

            self.correct.grid(row=2, column=0, pady=30)

            self.incorrect.grid(row=2, column=1)
            self.incorrect.config(padx=20, pady=10)
        self.get_next_question()
        self.window.mainloop()

    def ui_for_buttons(self):
        if question_data[QuizInterface.questionNumber]['type'] == "multiple":
            self.correct.grid_remove()
            self.incorrect.grid_remove()

            self.score_label.grid(row=0, column=3)
            self.canvas.grid(row=1, column=0, columnspan=4)
            self.option_a.config(text="A", highlightthickness=0, command=self.check_if_answer_option_a)
            self.option_a.grid(row=2, column=0)

            self.option_b.config(text="B", highlightthickness=0, command=self.check_if_answer_option_b)
            self.option_b.grid(row=2, column=1)

            self.option_c.config(text="C", highlightthickness=0, command=self.check_if_answer_option_c)
            self.option_c.grid(row=2, column=2)

            self.option_d.config(text="D", highlightthickness=0, command=self.check_if_answer_option_d)
            self.option_d.grid(row=2, column=3)

        else:
            self.option_a.grid_remove()
            self.option_b.grid_remove()
            self.option_c.grid_remove()
            self.option_d.grid_remove()
            self.score_label.grid(row=0, column=1)
            self.canvas.grid(row=1, column=0, columnspan=2)

            self.correct.config(text="TRUE", highlightthickness=0, command=self.check_if_answer_true)
            self.correct.grid(row=2, column=0, pady=30)

            self.incorrect.config(text="FALSE", highlightthickness=0, command=self.check_if_answer_false)
            self.incorrect.grid(row=2, column=1)
            self.incorrect.config(padx=20, pady=10)

    def get_next_question(self):
        QuizInterface.questionNumber += 1
        if self.quiz.still_has_questions():
            if question_data[QuizInterface.questionNumber]['type'] == "boolean":
                option = ""
                for i in range(0, 2):
                    option = f"{i + 1}. " + html.unescape(self.options[QuizInterface.questionNumber][i]) + " "
                self.correct.config(state="normal")
                self.incorrect.config(state="normal")
                if self.quiz.still_has_questions():
                    self.canvas.config(background="white")
                    q_text = self.quiz.next_question() + "\n" + option
                    self.canvas.itemconfig(self.question, text=q_text)
                else:
                    self.canvas.itemconfig(self.question, text=f"The quiz is Over Now.\nYour final score is {self.score}.")
                    self.correct.config(state="disabled")
                    self.incorrect.config(state="disabled")
            elif question_data[QuizInterface.questionNumber]['type'] == "multiple":
                option = ""
                for i in range(0, 4):
                    option += f"{i + 1}. " + html.unescape(self.options[QuizInterface.questionNumber][i]) + " \n"
                if self.quiz.still_has_questions():
                    self.canvas.config(background="white")
                    q_text = self.quiz.next_question() + "\n" + option
                    self.canvas.itemconfig(self.question, text=q_text)
                else:
                    self.canvas.itemconfig(self.question, text=f"The quiz is Over Now.\nYour final score is {self.score}.")
                    self.correct.config(state="disabled")
                    self.incorrect.config(state="disabled")

    def check_if_answer_true(self):
        self.correct.config(state="disabled")
        self.incorrect.config(state="disabled")
        if self.quiz.check_true_answer():
            self.canvas.config(background="green")
            self.score += 1
            self.score_label.config(text=f"Score: {self.score}")
        else:
            self.canvas.config(background="red")
        self.continue_after_delay()
        self.ui_for_buttons()

    def check_if_answer_false(self):
        self.correct.config(state="disabled")
        self.incorrect.config(state="disabled")
        if self.quiz.check_false_answer():
            self.canvas.config(background="green")
            self.score += 1
            self.score_label.config(text=f"Score: {self.score}")
        else:
            self.canvas.config(background="red")
        self.continue_after_delay()
        self.ui_for_buttons()

    def check_if_answer_option_a(self):
        self.option_a.config(state="normal")
        self.option_b.config(state="normal")
        self.option_c.config(state="normal")
        self.option_d.config(state="normal")
        if self.quiz.check_option_a():
            self.canvas.config(background="green")
            self.score += 1
            self.score_label.config(text=f"Score: {self.score}")
        else:
            self.canvas.config(background="red")
        self.continue_after_delay()
        self.ui_for_buttons()

    def check_if_answer_option_b(self):
        self.option_a.config(state="normal")
        self.option_b.config(state="normal")
        self.option_c.config(state="normal")
        self.option_d.config(state="normal")
        if self.quiz.check_option_b():
            self.canvas.config(background="green")
            self.score += 1
            self.score_label.config(text=f"Score: {self.score}")
        else:
            self.canvas.config(background="red")
        self.continue_after_delay()
        self.ui_for_buttons()

    def check_if_answer_option_c(self):
        self.option_a.config(state="normal")
        self.option_b.config(state="normal")
        self.option_c.config(state="normal")
        self.option_d.config(state="normal")
        if self.quiz.check_option_c():
            self.canvas.config(background="green")
            self.score += 1
            self.score_label.config(text=f"Score: {self.score}")
        else:
            self.canvas.config(background="red")
        self.continue_after_delay()
        self.ui_for_buttons()

    def check_if_answer_option_d(self):
        self.option_a.config(state="normal")
        self.option_b.config(state="normal")
        self.option_c.config(state="normal")
        self.option_d.config(state="normal")
        if self.quiz.check_option_d():
            self.canvas.config(background="green")
            self.score += 1
            self.score_label.config(text=f"Score: {self.score}")
        else:
            self.canvas.config(background="red")
        self.continue_after_delay()
        self.ui_for_buttons()

    def continue_after_delay(self):
        self.window.after(2000, self.get_next_question)
