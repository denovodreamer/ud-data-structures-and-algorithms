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

def check_number_type(number):

    number_type = None

    if number[0] == "(":         
        number_type = "fixed_line"
    elif " " in number:
        number_type = "mobile_number"
    elif number[:3] == "140":
        number_type = "telemarketers"
    
    return number_type


def check_telemarketers(calls):

    telemarketers = []

    for record in calls:
        incoming_number = record[0]

        if ((check_number_type(incoming_number) == "telemarketers")
                and (incoming_number not in telemarketers)):
            telemarketers.append(incoming_number)

    telemarketers = sorted(telemarketers)

    return telemarketers


def possible_telemarketers():

    telemarketers = check_telemarketers(calls)

    print("These numbers could be telemarketers: ")
    for telemarketer in telemarketers:
        print(telemarketer)


if __name__ == "__main__":
    possible_telemarketers()