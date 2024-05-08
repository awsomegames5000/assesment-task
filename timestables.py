import random


def ask_question(number, question_number):
    answer = int(input(f"What is {number} x {question_number}? "))
    correct_answer = number * question_number
    if answer == correct_answer:
        print("Correct")
        return True
    else:
        print(f"Incorrect, the answer is {correct_answer}.")
        return False


ans_correct = 0
for i in range(12):
    number = random.randint(1, 12)  
    question_number = random.randint(1, 12)
    if ask_question(number, question_number):
         ans_correct += 1
print(f"Test completed. Score is {ans_correct}/12")