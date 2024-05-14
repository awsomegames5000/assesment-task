import random
from tkinter import*

current_label = None

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
    
    
root=Tk()
root.title('Question')
root.geometry('400x400')
root.resizable(False, False)
#root.configure(bg='lightgray')

wid1=Entry(root, text='enter first number')
wid1.pack(pady=20)


label = Label(root)
label.pack()


Button1= Button(root, text='The button', command=root.quit)
Button1.pack()

result_label=Label(root, text='')
result_label.pack()

ans_correct=Label(root, text='')
ans_correct.pack()

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

root.mainloop()

