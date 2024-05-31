from tkinter import *
import random

root = Tk()

root.geometry('500x300')

root.title('Tkinter Math Operations Quiz')

root.resizable(False,False) # makes window of the program static; it cannot change.


def main():
    global homeframe #each frame corresponds to an interface shown in my storyboard. The frame acts as a master
                    #which contains the desired widgets I wish to keep and wipe out.

    homeframe = Frame(root,
                   bg='dark green',
                   width=500,height=300)
    homeframe.pack()
    homeframe.pack_propagate(0)#better catches the background colour as the frames of my program used to be controlled by its children.
                            #using this command, the program will stick to the original height and width that I set.

    title = Label(homeframe,  #customisations
                  bg='dark green',
                  text='Math Operation Quiz!',
                  font=('Arial',24,'bold'))
    title.pack()

    signs_labels = ['+', '-', 'x', '÷'] #create the list

    for signs in signs_labels: #create the loops which pack the lists

        button = Button(homeframe, 
                        text=signs, 
                        font=('Arial', 48,'bold'),
                        bg='maroon',
                        fg='white',
                        activebackground='VioletRed3',
                        command=lambda label=signs: choose_difficulty(label)) #lambda offers a buffer to the code which usually runs the 
        button.pack(side='left', padx=5, pady=5, expand = True, fill='both')    #next function rather than waiting for the user to click a button. This will return an operation parameter



def choose_difficulty(operation):
    global difficulty_frame #globally declared so the function can wipe the previous frame out
    global homeframe
    homeframe.pack_forget()

    difficulty_frame = Frame(root,
                             bg='dark green', 
                             width=500, height=300)
    difficulty_frame.pack()
    difficulty_frame.pack_propagate(0)

    difficulty_heading = Label(difficulty_frame, #Heading
                    bg='dark green', 
                    text='Select The Difficulty', 
                    font=('Arial', 24))
    difficulty_heading.pack(pady=20)

    difficulties = ['Easy', 'Medium', 'Hard'] #Create list
    for difficulty_options in difficulties: #Creates and packs the buttons from the list
        button = Button(difficulty_frame, 
                        text=difficulty_options, font=('Arial', 14),
                        bg='VioletRed3',
                        activebackground='maroon',
                        command=lambda difficulty=difficulty_options: run(operation, difficulty)) #carries operation and difficulty parameter
        button.pack(pady=10, expand=True, fill='both')



def run(operation,difficulty):
    global runframe
    global homeframe

    def incorrect():
        answer_label.config(text=f'Incorrect: The answer is {correct_answer}')
        error_label.config(text='')
        question_widget.delete(0, END)
        return False

    def ans_question():
        try: 
            answer = int(question_widget.get())
            if answer == correct_answer:
                answer_label.config(text='Correct')
                question_widget.delete(0, END)
                error_label.config(text='')
                return True
            else:
                incorrect()
        except ValueError:
            incorrect()
            error_label.config(text='Error, please input an integer number')

    difficulty_frame.pack_forget() #run function starts here, removing the difficulty frame from the program
    runframe = Frame(root,width=500,height=300,bg='dark green')
    runframe.pack()
    runframe.pack_propagate(0)

    #All widgets in this frame are packed with the side at the bottom to make it appearthat the question number is the heading (qnumber). I had reversed order of the widgets to make this work.
    question_number=Label(runframe, 
                      bg='dark green',
                      font=('Arial',24,'bold'),
                      text=f'Question 1')
    question_number.pack()

    answer_label = Label(runframe, #these labels are empty placeholders which will configure to 'correct' or 'incorrect' depending on the function
                              bg='dark green', 
                              font=('Arial',14))
    answer_label.pack()
    
    question_label = Label(runframe, #label packs the questions
                  bg='dark green',
                  font=('Arial',18))
    
    question_label.pack()
    question_widget=Entry(runframe, 
               font=('Arial',18),
               text='enter first number')
    question_widget.pack(expand=True) #entry widget for the answers

    Button1= Button(runframe, #button runs the function once user submits the answer
                    text='Enter',
                    font=('Arial',16),
                    bg='maroon',
                    activebackground='VioletRed3',
                    command=root.quit)
    Button1.pack(expand='true')

    error_label = Label(runframe, 
                  bg='dark green',
                  font=('Arial',12,'bold'),
                  )
    error_label.pack()

    score = Label(runframe, 
                  bg='dark green',
                  font=('Arial',12,'bold'),
                  text='0/12 correct')
    score.pack()

    ans_correct = 0
    for i in range(12):
        question_number.config(text=f'Question {i+1}')
        if difficulty == 'Easy': #the difficulty parameter was set in the previous frame and sets the range of numbers based on the chosen difficulty
            range1=12
            range2=40
        elif difficulty == 'Medium':
            range1=16
            range2=120
        else:
            range1=24
            range2=200

        if operation =='+': #the operation parameter was passed from the main menu page and uses if statements to go through the possible choices
            number1 = random.randint(10, range2)  
            number2 = random.randint(10, range2)
            correct_answer = number1 + number2
            question_label.config(text=f"What is {number1} + {number2}?")
        elif operation =='-':
            number1 = random.randint(10, range2)  
            number2 = random.randint(10, range2)
            correct_answer = number1 - number2
            question_label.config(text=f"What is {number1} - {number2}?")
        if operation =='x':
            number1 = random.randint(3, range1)  
            number2 = random.randint(3, range1)
            correct_answer = number1 * number2
            question_label.config(text=f"What is {number1} x {number2}?")
        elif operation =='÷':
            number1 = random.randint(3, range1)  
            number2 = random.randint(3, range1)
            product = number1 * number2
            correct_answer=product // number1 #this operation does the same as the normal division, but calculates using integers to remove decimal points.
            question_label.config(text=f"What is {product} ÷ {number1}? ")
        root.mainloop()
        if ans_question():
            ans_correct += 1
            score.config(text=f'{ans_correct}/12 correct')

    question_widget.pack_forget()    
    question_number.pack()
    Button1.config(text='Finish',command=lambda:finish(ans_correct,operation,difficulty)) #Once the test finishes, the button configures to move the program to the next frame



def finish(ans_correct, operation,difficulty):
    global runframe
    global finalframe

    runframe.pack_forget()

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
                  fg='white',
                  font=('Arial',24, 'bold'),
                  text=f'{ans_correct}/12')
    score.pack()
    MainMenu = Button(finalframe, 
                      bg='maroon',
                      fg='white',
                      activebackground='VioletRed3',
                      text='Main Menu', 
                      font=('Arial',14,'bold'),
                      command=res) #takes the program to the main menu
    
    MainMenu.pack(pady=20)


    retry = Button(finalframe, 
                   text='Try Again',
                   font=('Arial',14,'bold'),
                   bg='maroon',
                   fg='white' ,
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

    homeframe.pack()


main()

root.mainloop()
