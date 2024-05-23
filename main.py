from tkinter import *
import random

root = Tk()

root.geometry('500x250')

def main():
    global frame1
    global btn1
    global label

    frame1 = Frame(root,width=500,height=250,)
    frame1.pack()

    btn1 = Button(frame1,text='Start',command=run)
    btn1.pack(pady=20)

    label=Label(frame1,text='Multiplication Quiz')
    label.pack(expand=False)

def run():
    global framerun
    global frame1
    global result

    frame1.pack_forget()
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
        number = random.randint(1, 12)  
        number2 = random.randint(1, 12)
        label.config(text=f"What is {number} x {number2}?")
        root.mainloop()
        if ans_question():
            ans_correct += 1
    result=(f"Test completed: Score is {ans_correct}/12")
    Button1.config(text='proceed',command=lambda:finish())
    return result

def finish():
    global framerun
    global current_label
    global result
    global MainMenu
    global final_result

    current_label.pack_forget()
    framerun.pack_forget()
    finalframe=Frame(root,width=500,height=250)
    finalframe.pack(pady=20)
    final_result=Label(finalframe,text=result)
    final_result.pack()
    MainMenu=Button(text='main menu',command=res)
    MainMenu.pack()

def res():
    global frame1
    global btn1
    global label
    global MainMenu
    global final_result

    MainMenu.pack_forget()
    final_result.pack_forget()

    frame1.pack()

    btn1.pack(pady=20)

    label.pack(expand=False)

current_label=None
main()

root.mainloop()