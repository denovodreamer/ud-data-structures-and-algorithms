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

    telemarketers = set()

    for call in calls:
        calling_number = call[0]

        is_telemarketer = True

        for text_message in texts:
            sending_number = text_message[0]
            receiving_number = text_message[1]

            if calling_number == sending_number or calling_number == receiving_number:
                is_telemarketer = False
                break

        if is_telemarketer:
            telemarketers.add(calling_number)

    telemarketers = sorted(list(telemarketers))

    print("These numbers could be telemarketers: ")
    for telemarketer in telemarketers:
        print(telemarketer)


if __name__ == "__main__":
    possible_telemarketers(calls, texts)

