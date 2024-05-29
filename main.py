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
    frame1.pack_propagate(0)#better catches the background colour as the frames of my program used to be controlled by its children.
                            #using this command, the program will stick to the original height and width that I set.

    title = Label(frame1,  #customisations
                  bg='dark green',
                  text='Math Operation Quiz!',
                  font=('Arial',24,'bold'))
    title.pack()

    signs_labels = ['+', '-', 'x', '÷'] #create the list

    for signs in signs_labels: #create the loops which pack the lists

        button = Button(frame1, 
                        text=signs, 
                        font=('Arial', 48,'bold'),
                        bg='maroon',
                        fg='white',
                        activebackground='VioletRed3',
                        command=lambda label=signs: choose_difficulty(label)) #lambda offers a buffer to the code which usually runs the 
        button.pack(side='left', padx=5, pady=5, expand = True, fill='both')    #next function rather than waiting for the user to click a button. This will return an operation parameter

def choose_difficulty(operation):
    global difficulty_frame #globally declared so the function can wipe the previous frame out
    global frame1
    frame1.pack_forget()

    difficulty_frame = Frame(root,
                             bg='dark green', 
                             width=500, height=250)
    difficulty_frame.pack()
    difficulty_frame.pack_propagate(0)

    heading = Label(difficulty_frame, #Heading
                    bg='dark green', 
                    text='Select The Difficulty', 
                    font=('Arial', 24))
    heading.pack(pady=20)

    difficulties = ['Easy', 'Medium', 'Hard'] #Create list
    for options in difficulties: #Creates and packs the buttons from the list
        button = Button(difficulty_frame, 
                        text=options, font=('Arial', 14),
                        bg='VioletRed3',
                        activebackground='maroon',
                        command=lambda difficulty=options: run(operation, difficulty)) #carries operation and difficulty parameter
        button.pack(pady=5, expand=True, fill='x')

def run(operation,difficulty):
    global framerun
    global frame1

    def incorrect():
        current_label.config(text=f'Incorrect: The answer is {correct_answer}')
        wid1.delete(0, END)
        return False

    def ans_question():
        try: 
            answer = int(wid1.get())
            if answer == correct_answer:
                current_label.config(text='Correct')
                wid1.delete(0, END)
                return True
            else:
                incorrect()
        except ValueError:
            incorrect()

    difficulty_frame.pack_forget() #run function starts here, removing the difficulty frame from the program
    framerun = Frame(root,width=500,height=250,bg='dark green')
    framerun.pack()
    framerun.pack_propagate(0)

    #All widgets in this frame are packed with the side at the bottom to make it appear
    #that the question number is the heading (qnumber). I had reversed order of the widgets
    #to make this work.
    qnumber=Label(framerun, 
                      bg='dark green',
                      font=('Arial',24,'bold'),
                      text=f'question 1')
    qnumber.pack()

    current_label = Label(framerun, #these labels are empty placeholders which will configure to 'correct' or 'incorrect' depending on the function
                              bg='dark green', 
                              font=('Arial',14))
    current_label.pack()
    
    label = Label(framerun, #label packs the questions
                  bg='dark green',
                  font=('Arial',18))
    
    label.pack()
    wid1=Entry(framerun, 
               font=('Arial',18),
               text='enter first number')
    wid1.pack(expand=True) #entry widget for the answers

    Button1= Button(framerun, #button runs the function once user submits the answer
                    text='Enter',
                    font=('Arial',16),
                    bg='maroon',
                    activebackground='VioletRed3',
                    command=root.quit)
    Button1.pack(expand='true')

    score = Label(framerun, 
                  bg='dark green',
                  font=('Arial',12,'bold'),
                  text='0/12 correct')
    score.pack()

    ans_correct = 0
    for i in range(12):
        qnumber.config(text=f'question {i+1}')
        if difficulty == 'Easy': #the difficulty parameter was set in the previous frame and sets the range of numbers based on the chosen difficulty
            range1=10
            range2=40
        elif difficulty == 'Medium':
            range1=15
            range2=100
        else:
            range1=20
            range2=150

        if operation =='+': #the operation parameter was passed from the main menu page and uses if statements to go through the possible choices
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
        elif operation =='÷':
            number1 = random.randint(1, range1)  
            number2 = random.randint(1, range1)
            product = number1 * number2
            correct_answer=product // number1 #this operation does the same as the normal division, but calculates using integers to remove decimal points.
            label.config(text=f"What is {product} ÷ {number1}? ")
        root.mainloop()
        if ans_question():
            ans_correct += 1
            score.config(text=f'{ans_correct}/12 correct')
            
    qnumber.pack()
    Button1.config(text='Finish',command=lambda:finish(ans_correct,operation,difficulty)) #Once the test finishes, the button configures to move the program to the next frame

def finish(ans_correct, operation,difficulty):
    global framerun
    global finalframe

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

    score = Label(finalframe, #score label takes ans_correct parameter to display
                  bg='dark green',
                  font=('Arial',24, 'bold'),
                  text=f'{ans_correct}/12')
    score.pack()
    MainMenu = Button(finalframe, 
                      bg='maroon',
                      activebackground='VioletRed3',
                      text='Main Menu', 
                      font=('Arial',14),
                      command=res) #takes the program to the main menu
    
    MainMenu.pack(pady=20)
    retry = Button(finalframe, 
                   text='Try Again',
                   font=('Arial',14),
                   bg='maroon', 
                   activebackground='VioletRed3',
                   command=lambda:restart(operation,difficulty))
    retry.pack()

def restart(operation,difficulty): #This function removes the previous frame and restarts the run function while taking the parameters the user chose.
    global finalframe

    finalframe.pack_forget()

    run(operation,difficulty)
    

def res(): #This function removes the previous frame but takes the user to the main menu frame.
    global finalframe

    finalframe.pack_forget()

    frame1.pack()


main()

root.mainloop()
