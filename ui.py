from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain:QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        
        self.score_label = Label(text=f"Score : {self.quiz.score}",fg="white", bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)
        
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question = self.canvas.create_text(150, 125, text="asw", font=("Arial",20,"italic"), fill=THEME_COLOR, width=280)
        self.canvas.grid(column=0,row=1,columnspan=2)
        
        right_img = PhotoImage(file="./images/true.png")
        self.right_btn = Button(image = right_img, command=self.true_option)
        self.right_btn.grid(column=0, row=2,pady=50)
        
        wrong_img = PhotoImage(file="./images/false.png")
        self.wrong_btn = Button(image = wrong_img, command=self.false_option)
        self.wrong_btn.grid(column=1, row=2)
        
        self.get_next_question()
        
        self.window.mainloop()
        
    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score : {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text = q_text)
        else:
            self.canvas.itemconfig(self.question, text = "Yo've reached end of the quiz")
            self.right_btn.config(state="disabled")
            self.wrong_btn.config(state="disabled")
        
    def true_option(self):
        self.give_feedback(self.quiz.check_answer("True")) 
        
    def false_option(self):
        self.give_feedback(self.quiz.check_answer("False"))
        
    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
            
        self.window.after(1000, self.get_next_question)
