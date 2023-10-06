"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

def numbers_in(records, telephone_numbers):

    for record in records:
        incoming_number = record[0]
        answering_number = record[1]

        if incoming_number not in telephone_numbers:
            telephone_numbers.append(incoming_number)

        if answering_number not in telephone_numbers:
            telephone_numbers.append(answering_number)

    return telephone_numbers


def count_numbers(texts, calls):
    telephone_numbers = []

    telephone_numbers = numbers_in(texts, telephone_numbers)
    telephone_numbers = numbers_in(calls, telephone_numbers)

    return len(telephone_numbers)


n = count_numbers(texts, calls)

print(f"There are {n} different telephone numbers in the records.")