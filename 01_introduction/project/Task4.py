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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""


def possible_telemarketers(calls, texts):

    # All numbers sending or receiving messages
    text_numbers = []
    for text_message in texts:
        sending_number = text_message[0]
        receiving_number = text_message[1]

        text_numbers.append(sending_number)
        text_numbers.append(receiving_number)

    # All calling numbers and all receiving numbers
    calling_numbers = []
    receiving_numbers = []
    for call in calls:
        calling_number = call[0]
        receiving_number = call[1]

        calling_numbers.append(calling_number)
        receiving_numbers.append(receiving_number)

    # Select numbers that only call
    telemarketers = []
    for calling_number in calling_numbers:
        if calling_number in text_numbers:
            continue
        
        if calling_number in receiving_numbers:
            continue

        telemarketers.append(calling_number)

    telemarketers = sorted(list(telemarketers))

    print("These numbers could be telemarketers: ")
    for telemarketer in telemarketers:
        print(telemarketer)


if __name__ == "__main__":
    possible_telemarketers(calls, texts)

