import random


def ask_question():
    try:
        if question == '*':
            number1 = random.randint(1, 12)  
            number2 = random.randint(1, 12)
            answer = int(input(f"What is {number1} x {number2}? "))
            correct_answer = number1 * number2
        elif question == '+':
            number1 = random.randint(1, 100)  
            number2 = random.randint(1, 100)
            answer = int(input(f"What is {number1} + {number2}? "))
            correct_answer = number1 + number2
        elif question == '-':
            number1 = random.randint(1, 100)  
            number2 = random.randint(1, 100)
            answer = int(input(f"What is {number1} - {number2}? "))
            correct_answer = number1 - number2
        else:
            number1 = random.randint(1, 12)  
            number2 = random.randint(1, 12)
            product=number1*number2
            correct_answer=product / number1
            answer = int(input(f"What is {product} / {number1}? "))
        if answer == correct_answer:
            print("Correct")
            return True
        else:
            print(f"Incorrect, the answer is {correct_answer}.")
            return False
    except ValueError:
        print(f"Incorrect, the answer is {correct_answer}.")
        return False


ans_correct = 0
question=input('what operation would you like to practice (+,-,*,/)')
for i in range(12):
    if ask_question():
         ans_correct += 1
print(f"Test completed. Score is {ans_correct}/12")