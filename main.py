from tkinter import *
import random

root = Tk()

root.geometry('500x250')

def main():
    frame1 = Frame(root,width=500,height=250,)
    frame1.pack()

    btn1 = Button(frame1,text='main page',command=main)
    btn1.pack(expand=False)
    btn2 = Button(frame1,text='other page',command=other)
    btn2.pack(expand=False)

    label=Label(frame1,text='hello')
    label.pack(expand=False)

def other():

    def incorrect():
        global current_label
        if current_label:
                current_label.pack_forget()
        correct_answer = number * number2
        current_label = Label(root, text=f"Incorrect, the answer is {correct_answer}.")
        current_label.pack()
        wid1.delete(0, END)
        return False

    def ans_question():
        try: 
            global current_label
            if current_label:
                current_label.pack_forget()
            answer = int(wid1.get())
            correct_answer = number * number2
            if answer == correct_answer:
                current_label = Label(root, text='Correct')
                current_label.pack()
                wid1.delete(0, END)
                return True
            else:
                incorrect()
        except ValueError:
            incorrect()


    framerun = Frame(root,width=500,height=250)
    framerun.pack()

    wid1=Entry(framerun, text='enter first number')
    wid1.pack(pady=20)


    label = Label(framerun)
    label.pack()


    Button1= Button(framerun, text='The button', command=root.quit)
    Button1.pack()

    result_label=Label(root, text='')
    result_label.pack()

    ans_correct = 0
    for i in range(12):
        number = random.randint(1, 12)  
        number2 = random.randint(1, 12)
        label.config(text=f"What is {number} x {number2}?")
        root.mainloop()
        if ans_question():
            ans_correct += 1
    question=Label(root, text=f"Test completed: Score is {ans_correct}/12")
    question.pack()
    Button1.config(command=lambda:None)

current_label=None
main()

root.mainloop()