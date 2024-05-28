from tkinter import *
import random

root = Tk()

root.geometry('500x250')

root.resizable(False,False)

def main():
    global frame1

    frame1 = Frame(root,bg='green',width=500,height=250)
    frame1.pack()
    frame1.pack_propagate(0)

    title = Label(frame1, bg='green',text='Math Operation Quiz!',font=('Arial',24))
    title.pack()

    signs_labels = ['+', '-', 'x', '÷']

    buttons = []

    for signs in signs_labels:
        button = Button(frame1, text=signs, font=('Arial', 30),command=lambda label=signs: run(label))
        buttons.append(button)
        button.pack(side=LEFT, padx=5, pady=5, expand = True, fill='both')

def run(operation):
    global framerun
    global frame1
    global qnumber

    def incorrect():
        global current_label
        if current_label:
            current_label.pack_forget()
        current_label = Label(root, text=f'Incorrect. The answer is {correct_answer}')
        current_label.pack()
        wid1.delete(0, END)
        return False

    def ans_question():
        try: 
            global current_label
            if current_label:
                current_label.pack_forget()
            answer = int(wid1.get())
            if answer == correct_answer:
                current_label = Label(root, text='Correct')
                current_label.pack()
                wid1.delete(0, END)
                return True
            else:
                incorrect()
        except ValueError:
            incorrect()

    frame1.pack_forget()
    framerun = Frame(root,width=500,height=250)
    framerun.pack()

    wid1=Entry(framerun, text='enter first number')
    wid1.pack(pady=20)


    label = Label(framerun)
    label.pack(pady=20)

    Button1= Button(framerun, text='The button', command=root.quit)
    Button1.pack()

    ans_correct = 0
    for i in range(12):
        if qnumber:
            qnumber.pack_forget()
        qnumber=Label(framerun,text=f'question {i+1}')
        qnumber.pack()
        if operation =='x':
            number = random.randint(1, 12)  
            number2 = random.randint(1, 12)
            correct_answer = number * number2
            label.config(text=f"What is {number} x {number2}?")
        elif operation =='+':
            number = random.randint(1, 100)  
            number2 = random.randint(1, 100)
            correct_answer = number + number2
            label.config(text=f"What is {number} + {number2}?")
        elif operation =='-':
            number = random.randint(1, 100)  
            number2 = random.randint(1, 100)
            correct_answer = number - number2
            label.config(text=f"What is {number} - {number2}?")
        else:
            number1 = random.randint(1, 12)  
            number2 = random.randint(1, 12)
            product = number1 * number2
            correct_answer=product // number1
            label.config(text=f"What is {product} ÷ {number1}? ")
        root.mainloop()
        if ans_question():
            ans_correct += 1
            
    Button1.config(text='Finish',command=lambda:finish(ans_correct,operation))

def finish(ans_correct, operation):
    global framerun
    global current_label
    global finalframe

    if current_label:
        current_label.pack_forget()
    framerun.pack_forget()

    finalframe = Frame(root, width=500, height=250)
    finalframe.pack(pady=20)
    final_result = Label(finalframe, text=f"Test completed: Score is {ans_correct}/12")
    final_result.pack()
    MainMenu = Button(finalframe, text='Main Menu', command=res)
    MainMenu.pack()
    retry = Button(finalframe, text='Try Again', command=lambda:restart(operation))
    retry.pack()

def restart(operation):
    global finalframe

    finalframe.pack_forget()

    run(operation)
    

def res():
    global finalframe

    finalframe.pack_forget()

    frame1.pack()

current_label=None
qnumber = None
main()

root.mainloop()

#DECORATE!!!!!!!!!!!!
