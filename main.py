import random

def menu():
    global lst_of_numbers
    min_number_query = input('What is the minimum number you want me to guess?\n')
    max_number_query = input('What is the maximum number you want me to guess?\n')
    if min_number_query >= max_number_query:
        print("That's an invalid choice, please try again..")
        menu()
    else:
        numbers = range(int(min_number_query), int(max_number_query) + 1)
        for number in numbers:
            lst_of_numbers.append(number)
        guess()

lst_of_numbers = []
count = 0

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


menu()