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

    print(len(telemarketers))

    print("These numbers could be telemarketers: ")
    for telemarketer in telemarketers:
        print(telemarketer)


if __name__ == "__main__":
    possible_telemarketers(calls, texts)



# def check_calls(calls):

#     calling_numbers = set()

#     for record in calls:
#         calling_number = record[0]
#         calling_numbers.add(calling_number)

#     return calling_numbers


# def check_texts(texts):

#     numbers = set()

#     for record in texts:
#         sending_number = record[0]
#         numbers.add(sending_number)

#         receiving_number = record[1]
#         numbers.add(receiving_number)

#     return numbers


# def check_telemarketers(calls, texts):

#     calling_numbers = check_calls(calls)
#     text_numbers = check_texts(texts)

#     telemarketers = calling_numbers - text_numbers

#     return telemarketers


# def possible_telemarketers():

#     telemarketers = check_telemarketers(calls, texts)

#     print("These numbers could be telemarketers: ")
#     for telemarketer in telemarketers:
#         print(telemarketer)


# if __name__ == "__main__":
#     possible_telemarketers()




# def check_number_type(number):

#     number_type = None

#     if number[0] == "(":         
#         number_type = "fixed_line"
#     elif " " in number:
#         number_type = "mobile_number"
#     elif number[:3] == "140":
#         number_type = "telemarketers"
    
#     return number_type


# def check_telemarketers(calls):

#     telemarketers = []

#     for record in calls:
#         incoming_number = record[0]

#         if ((check_number_type(incoming_number) == "telemarketers")
#                 and (incoming_number not in telemarketers)):
#             telemarketers.append(incoming_number)

#     telemarketers = sorted(telemarketers)

#     return telemarketers


# def possible_telemarketers():

#     telemarketers = check_telemarketers(calls)

#     print("These numbers could be telemarketers: ")
#     for telemarketer in telemarketers:
#         print(telemarketer)


# if __name__ == "__main__":
#     possible_telemarketers()