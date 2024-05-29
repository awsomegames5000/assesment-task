from tkinter import *
import random

root = Tk()

root.geometry('500x250')

root.resizable(False,False) # makes window of the program static; it cannot change.


def main():
    global frame1 #each frame corresponds to an interface shown in my storyboard. The frame acts as a master
                    #which contains the desired widgets I wish to keep and wipe out.

    frame1 = Frame(root,
                   bg='dark green',
                   width=500,height=250)
    frame1.pack()
    frame1.pack_propagate(0)

    title = Label(frame1, 
                  bg='dark green',
                  text='Math Operation Quiz!',
                  font=('Arial',24,'bold'))
    title.pack()

    signs_labels = ['+', '-', 'x', '÷']

    for signs in signs_labels:

        button = Button(frame1, 
                        text=signs, 
                        font=('Arial', 48,'bold'),
                        bg='maroon',
                        fg='white',
                        activebackground='VioletRed3',
                        command=lambda label=signs: choose_difficulty(label))
        button.pack(side=LEFT, padx=5, pady=5, expand = True, fill='both')

def choose_difficulty(operation):
    global difficulty_frame
    global frame1
    frame1.pack_forget()

    difficulty_frame = Frame(root,
                             bg='dark green', 
                             width=500, height=250)
    difficulty_frame.pack()
    difficulty_frame.pack_propagate(0)

    heading = Label(difficulty_frame,
                    bg='dark green', 
                    text='Select The Difficulty', 
                    font=('Arial', 24))
    heading.pack(pady=20)

    difficulties = ['Easy', 'Medium', 'Hard']
    for options in difficulties:
        button = Button(difficulty_frame, 
                        text=options, font=('Arial', 14),
                        bg='VioletRed3',
                        activebackground='maroon',
                        command=lambda difficulty=options: run(operation, difficulty))
        button.pack(pady=5, expand=True, fill='x')

def run(operation,difficulty):
    global framerun
    global frame1
    global qnumber

    def incorrect():
        global current_label
        if current_label:
            current_label.pack_forget()
        current_label = Label(framerun, 
                              bg='dark green', 
                              font=('Arial',14),
                              text=f'Incorrect. The answer is {correct_answer}')
        current_label.pack(side='bottom')
        wid1.delete(0, END)
        return False

    def ans_question():
        try: 
            global current_label
            if current_label:
                current_label.pack_forget()
            answer = int(wid1.get())
            if answer == correct_answer:
                current_label = Label(framerun,
                                      bg='dark green', 
                                      font=('Arial',14),
                                      text='Correct')
                current_label.pack(side='bottom')
                wid1.delete(0, END)
                return True
            else:
                incorrect()
        except ValueError:
            incorrect()

    difficulty_frame.pack_forget()
    framerun = Frame(root,width=500,height=250,bg='dark green')
    framerun.pack()
    framerun.pack_propagate(0)

    #All widgets in this frame are packed with the side at the bottom to make it appear
    #that the question number is the heading (qnumber). I had reversed order of the widgets
    #to make this work.
    Button1= Button(framerun, 
                    text='Enter',
                    font=('Arial',16),
                    bg='maroon',
                    activebackground='VioletRed3',
                    command=root.quit)
    Button1.pack(side='bottom',expand='true')

    wid1=Entry(framerun, 
               font=('Arial',18),
               text='enter first number')
    wid1.pack(side='bottom',expand=True)

    label = Label(framerun, 
                  bg='dark green',
                  font=('Arial',18))
    label.pack(side='bottom')


    ans_correct = 0
    for i in range(12):
        if qnumber:
            qnumber.pack_forget()
        qnumber=Label(framerun, 
                      bg='dark green',
                      font=('Arial',24,'bold'),
                      text=f'question {i+1}')
        qnumber.pack(side='bottom')

        if difficulty == 'Easy':
            range1=12
            range2=50
        elif difficulty == 'Medium':
            range1=18
            range2=100
        else:
            range1=24
            range2=200

        if operation =='+':
            number = random.randint(1, range2)  
            number2 = random.randint(1, range2)
            correct_answer = number + number2
            label.config(text=f"What is {number} + {number2}?")
        elif operation =='-':
            number = random.randint(1, range2)  
            number2 = random.randint(1, range2)
            correct_answer = number - number2
            label.config(text=f"What is {number} - {number2}?")
        if operation =='x':
            number = random.randint(1, range1)  
            number2 = random.randint(1, range1)
            correct_answer = number * number2
            label.config(text=f"What is {number} x {number2}?")
        else:
            number1 = random.randint(1, range1)  
            number2 = random.randint(1, range1)
            product = number1 * number2
            correct_answer=product // number1
            label.config(text=f"What is {product} ÷ {number1}? ")
        root.mainloop()
        if ans_question():
            ans_correct += 1
    current_label.pack_forget()
            
    qnumber.pack()
    Button1.config(text='Finish',command=lambda:finish(ans_correct,operation,difficulty))

def finish(ans_correct, operation,difficulty):
    global framerun
    global current_label
    global finalframe

    if current_label:
        current_label.pack_forget()
    framerun.pack_forget()

    finalframe = Frame(root, 
                       bg='dark green',
                       width=500, height=300)
    finalframe.pack()
    finalframe.pack_propagate(0)

    final_result = Label(finalframe,
                         bg='dark green',
                         font=('Arial',24),
                        text="Test completed, your Score is:")
    final_result.pack()

    score = Label(finalframe,
                  bg='dark green',
                  font=('Arial',24, 'bold'),
                  text=f'{ans_correct}/12')
    score.pack()
    MainMenu = Button(finalframe, 
                      bg='maroon',
                      activebackground='VioletRed3',
                      text='Main Menu', 
                      font=('Arial',14),
                      command=res)
    
    MainMenu.pack(pady=20)
    retry = Button(finalframe, 
                   text='Try Again',
                   font=('Arial',14),
                   bg='maroon', 
                   activebackground='VioletRed3',
                   command=lambda:restart(operation,difficulty))
    retry.pack()

def restart(operation,difficulty):
    global finalframe

    finalframe.pack_forget()

    run(operation,difficulty)
    

def res():
    global finalframe

    finalframe.pack_forget()

    frame1.pack()

current_label=None
qnumber = None
main()

root.mainloop()
