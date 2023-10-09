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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore. In other words, the calls were initiated by "(080)" area code
to the following area codes and mobile prefixes:
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""


################################################
# Resolution
################################################

def check_number_type(number):

    number_type = None

    if number[0] == "(":         
        number_type = "fixed_line"
    elif " " in number:
        number_type = "mobile_number"
    elif number[:3] == "140":
        number_type = "telemarketers"
    
    return number_type


def get_area_code(fixed_line_number):
    
    area_code = fixed_line_number.split(")")[0][1:]

    if area_code[0] != "0":
        return

    return area_code


def get_area_code_prefix(mobile_number):

    prefix = mobile_number.split(" ")[0]

    if prefix[0] not in ["7", "8", "9"] or "(" in mobile_number:
        return

    area_code = prefix[:-1]

    return area_code


def extract_number_code(number):
    code = None

    number_type = check_number_type(number)

    if number_type == "fixed_line":
        code = get_area_code(number)
    elif number_type == "mobile_number":
        code = get_area_code_prefix(number)
    elif number_type == "telemarketers":
        code = "140"

    return code


def bangalore_calls(calls):

    codes = []
    codes_bangalore = []

    number_of_bengalore_calls = 0

    for calling_number, receiving_number, _, _ in calls:
        if extract_number_code(calling_number) == "080":
            code = extract_number_code(receiving_number)
            if code not in codes:
                codes.append(code)
            if code == "080":
                codes_bangalore.append(code)

            number_of_bengalore_calls += 1

    codes = sorted(codes)

    percentage = round((len(codes_bangalore)/number_of_bengalore_calls)*100, 2)

    return codes, percentage


def find_all_codes():
    codes, percentage = bangalore_calls(calls)
    print(len(calls))
    print("The numbers called by people in Bangalore have codes:")
    # for code in codes:
    #     print(code)
    print(f"{percentage} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")


if __name__ == "__main__":
    find_all_codes()



################################################
# Tests 
################################################

def test_extract_number_code():
    assert "0824" == extract_number_code("(0824)6366719")
    assert "084" == extract_number_code("(084)6366719")
    assert "97411" == extract_number_code("97411 71155")
    assert "140" == extract_number_code("1408371942")
    print("Extract code passed!")


def test_get_prefix():
    assert "9741" == get_area_code_prefix("97411 71155")
    assert get_area_code_prefix("7411 71155") is None
    print("Prefix passed!")


def test_number_type():
    assert check_number_type("1408371942") == "telemarketers"
    assert check_number_type("(0824)6366719") == "fixed_line"
    assert check_number_type("93427 56500") == "mobile_number"
    print("Number type passed!")


def test_get_area_code():
    assert "0824" == get_area_code("(0824)6366719")
    print("Get area code Passed!")


