import random

lst_of_numbers = []
count = 0

numbers = range(1,101)
for number in numbers:
    lst_of_numbers.append(number)

def query(random_number):
    global lst_of_numbers
    global count
    user_query = input()
    if user_query == 'High' or user_query == 'high':
        index = lst_of_numbers.index(random_number)
        lst_of_numbers = lst_of_numbers[:index]
        count += 1
        guess()
    elif user_query == 'Low' or user_query == 'low':
        index = lst_of_numbers.index(random_number)
        lst_of_numbers = lst_of_numbers[index + 1:]
        count += 1
        guess()
    elif user_query == 'correct' or user_query == 'Correct' or user_query == 'yes' or user_query == "Yes":
        print(f"I guessed your number in {count} guesses!")
    else:
        print("I'm sorry, can you try that again?")
        query(random_number)


def guess():
    global lst_of_numbers
    global count
    count += 1
    random_number = random.choice(lst_of_numbers)
    print(random_number)
    query(random_number)


guess()