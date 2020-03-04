import tkinter
from tkinter import *
import random

questions = [
    "What is the highest number used in a Sudoku puzzle?",
    "What is the term for a positive electrode?",
    "Which swimming stroke is named after an insect?",
    "Which English queen has the same name as a type of plum?",
    "How many dots are used in each letter in the Braille system?",
    "Which movie won the Oscar for best actor, director and cinematography in 2016?",
    "What is a female deer called?",
    "What unit is used to measure horses?",
    "What are birds of a feather said to do?",
    "Betz cells are found in which part of the body?",
]

answers_choice = [
    ["Eight","Ten","Four","Nine"],
    ["Electrolyte","Anode","Cathode","Electrode"],
    ["Butterfly","Ant","Bug","Beetal"],
    ["Victoria","Elizabeth","Lady Macbeth","Queen Victoria 2"],
    ["8","6","3","4"],
    ["Life of Pie","Dunkrik","Joker","The Revenant"],
    ["Tadpole","Lamb","Doe","Kitten"],
    ["Feet","Hands","Km","Mile"],
    ["Cecilia","Elton John","True Blue","Blue Buddha"],
    ["The Brain","Lungs","Kidney","Spinal Cord"],
]

answers = [3,1,0,0,1,3,2,1,0,0]

indexes = []

user_answer = []


def generator():
    global indexes
    while len(indexes) < 10:
        x = random.randint(0,9)
        if x in indexes:
            continue
        else:
            indexes.append(x)


def showresult(score):
    labelquestions.destroy()
    r1.destroy()
    r2.destroy()
    r3.destroy()
    r4.destroy()

    labelresulttext = Label(
        root,
        font=("Times",24),
        background="#ffffff",
    )
    labelresulttext.pack(pady=(350,0))
    if score >=15:
         # labelresulttext.configure(text="Congratulations you are GREAT !!!")
         labelresulttext.configure(text="Congratulations you have scored " + str(score) + " marks.")
    elif 8 <= score < 15:
         # labelresulttext.configure(text="You can do BETTER !!!")
         labelresulttext.configure(text="Your score is " + str(score) + " marks... \nYou can do BETTER !!!")
    else:
         # labelresulttext.configure(text="You need to work HARDER !!!")
         labelresulttext.configure(text="Your score is " + str(score) + " marks... \nYou need to work HARDER !!!")


def calc():
    global indexes,user_answer,answers
    x = 0
    score = 0
    for i in indexes:
        if user_answer[x] == answers[i]:
            score = score + 2
        x += 1
    print(score)
    showresult(score)


ques = 1


def selected():
    global radiovar,user_answer
    global labelquestions,r1,r2,r3,r4
    global ques
    x = radiovar.get()
    user_answer.append(x)
    radiovar.set(-1)
    if ques < 10:
        labelquestions.config(text=questions[indexes[ques]])
        r1["text"] = answers_choice[indexes[ques]][0]
        r2["text"] = answers_choice[indexes[ques]][1]
        r3["text"] = answers_choice[indexes[ques]][2]
        r4["text"] = answers_choice[indexes[ques]][3]
        ques += 1
    else:
        calc()


def startquiz():
    global labelquestions,r1,r2,r3,r4
    labelquestions = Label(
        root,
        text=questions[indexes[0]],
        font=("Consolas", 18),
        width=500,
        justify="center",
        wraplength=700,
        background="#ffffff",
    )
    labelquestions.pack(pady=(200,0))

    global radiovar
    radiovar = IntVar()
    radiovar.set(-1)

    r1 = Radiobutton(
        root,
    text=answers_choice[indexes[0]][0],
        font=("Times", 16),
        value=0,
        variable=radiovar,
        command=selected,
        background="#ffffff"
    )
    r1.pack(pady=3)

    r2 = Radiobutton(
        root,
        text=answers_choice[indexes[0]][1],
        font=("Times", 16),
        value=1,
        variable=radiovar,
        command=selected,
        background="#ffffff"
    )
    r2.pack(pady=3)

    r3 = Radiobutton(
        root,
        text=answers_choice[indexes[0]][2],
        font=("Times", 16),
        value=2,
        variable=radiovar,
        command=selected,
        background="#ffffff"
    )
    r3.pack(pady=3)

    r4 = Radiobutton(
        root,
        text=answers_choice[indexes[0]][3],
        font=("Times", 16),
        value=3,
        variable=radiovar,
        command=selected,
        background="#ffffff"
    )
    r4.pack(pady=3)


def startispressed():
    labelimage.destroy()
    labeltext.destroy()
    labelInstruction.destroy()
    labelRules.destroy()
    btnStart.destroy()
    generator()
    startquiz()


root = tkinter.Tk()
root.title("Quiz App")
root.geometry("700x800")
root.config(background="#ffffff")
root.resizable(0, 0)

img1 = PhotoImage(file="a.png")
labelimage = Label(
    root,
    image=img1,
    background="#ffffff"
)
labelimage.pack(pady=(30, 0))

labeltext = Label(
    root,
    text="QuizApp",
    font=("Comic sans MS", 24, "bold"),
    background="#ffffff"
)
labeltext.pack(pady=(0, 30))

img2 = PhotoImage(file="start.png")
btnStart = Button(
    root,
    image=img2,
    relief=FLAT,
    border=0,
    command=startispressed,
)
btnStart.pack()

labelInstruction = Label(
    root,
    text="Read the Instructions.\nClick start once you are Ready.",
    background="#ffffff",
    font=("Consolas", 14),
    justify="center",
)
labelInstruction.pack(pady=(0, 60))

labelRules = Label(
    root,
    text="This quiz contains 10 questions.\n"
         "You will get 20 seconds to solve a question.\n"
         "Once you select a radio button it will be a final answer.\nSo think before you select.",
    width=100,
    font=("Times", 14, "bold"),
    background="#ffffff"
)
labelRules.pack()

root.mainloop()
