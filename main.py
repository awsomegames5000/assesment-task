from tkinter import *
import random

root = Tk()

root.geometry('500x250')

def main():
    global frame1

    frame1 = Frame(root)
    frame1.pack()

    signs_labels = ['+', '-', '*', '/']

    buttons = []

    for signs in signs_labels:
        button = Button(frame1, text=signs, command=lambda label=signs: run(label))
        button.pack(side=LEFT, padx=5)
        buttons.append(button)

def run(operation):
    global framerun
    global frame1

    frame1.pack_forget()

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
        if operation =='*':
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
            label.config(text=f"What is {product} / {number1}? ")
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
main()

root.mainloop()

#DECORATE!!!!!!!!!!!!
