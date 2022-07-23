from tkinter import *
from tkinter import font
from Question import *
import random


Desired_font = ("Comic Sans MS", 10, "bold")

def start_again():
    global Score,Question_no
    
    Score = 0
    Question_no = 1
    next_b.config(text="next")
    val1.set(0)
    val2.set(0)
    val3.set(0)
    question.config(text=Questions[Question_no-1].get_question())
    option1.config(text=Questions[Question_no-1].get_option1())
    option2.config(text=Questions[Question_no-1].get_option2())
    option3.config(text=Questions[Question_no-1].get_option3())
    play_again.place_forget()
    score_output.place_forget()
    root.pack()
    
def next():
    global Score,Question_no
    if(val1.get()):
        selected_option = 0
    elif(val2.get()):
        selected_option = 1
    elif(val3.get()):
        selected_option = 2
    else:
        selected_option = -1

    if Questions[Question_no-1].answer_check(selected_option):
        Score += 1

    if(Question_no == Total_No_Questions-1):
        next_b.config(text="Submit")
    Question_no = Question_no + 1

    

    if(Question_no > Total_No_Questions):
        root.pack_forget()
        score_output.place(relx=.45,rely=.30)
        play_again.place(relx = .45,rely = .60)
        score_output.config(text = "Score: " +str(Score))

    else:
        val1.set(0) 
        val2.set(0) 
        val3.set(0) 
        question.config(text=Questions[Question_no-1].get_question())
        option1.config(text=Questions[Question_no-1].get_option1())
        option2.config(text=Questions[Question_no-1].get_option2())
        option3.config(text=Questions[Question_no-1].get_option3())

def Check(Option):
    if(Option == 1):
        # val1.set(1)
        val2.set(0)
        val3.set(0)
        
        
    elif(Option == 2):
        val1.set(0)
        # val2.set(1)
        val3.set(0)
      
    elif(Option == 3):
        val1.set(0)
        val2.set(0)
        # val3.set(1)
        
num1 = random.randint(1, 9)
num2 = random.randint(1, 9)
num3 = random.randint(1, 9)
num4 = random.randint(1, 9)
num5 = random.randint(1, 9)
num6 = random.randint(1, 9)

q1= Question("What is " + str(num1) + "+" + str(num2) +"?" , [num1 + num2, num1 * num2,num1 -num2])
q2= Question("What is " + str(num3) + "-" + str(num4) +"?" , [num3 -num4, num3 * num4, num3 + num4])
q3= Question("What is " + str(num5) + "*" + str(num6) +"?" , [num5 * num6, num5 + num6,num5 -num6])
Questions = [q1, q2, q3]

        


Score = 0
Total_No_Questions = 3
Question_no = 1

Win= Tk()
Win.geometry("500x300")
Win.title("Basic Math quiz")

label = Label(
    text="Welcome to a Basic Math quiz"
)
label.configure(font = Desired_font)
label.pack()

label = Label(
    text="   "
)
label.configure(font = Desired_font)
label.pack()

root = Frame(Win)
root.pack()


question = Label(root,width = 60,font=(10),text=Questions[0].get_question())
question.configure(font = Desired_font)
question.pack(fill=X)

val1 = IntVar()
val2 = IntVar()
val3 = IntVar()

option1 = Checkbutton(root,variable=val1,text=Questions[Question_no-1].get_option1(),command=lambda:Check(1))
option1.pack()

option2 = Checkbutton(root,variable=val2,text=Questions[Question_no-1].get_option2(),command=lambda:Check(2))
option2.pack()

option3 = Checkbutton(root,variable=val3,text=Questions[Question_no-1].get_option3(),command=lambda:Check(3))
option3.pack()

next_b = Button(root , text = "Submit",command=next)
next_b.configure(font = Desired_font)
next_b.pack()



score_output = Label(Win,font=(50))
score_output.configure(font = Desired_font)
score_output.place_forget()



play_again = Button(Win,text= "Play Again",command=start_again)
play_again.configure(font = Desired_font)
play_again.place_forget()

label = Label(
    
)

label.pack()
Win.mainloop()