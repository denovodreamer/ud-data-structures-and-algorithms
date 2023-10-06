"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""


def update_number(total_durations, number, duration):

    duration = int(duration)
    durations = dict(total_durations)

    if number not in total_durations:
        durations[number] = duration
    else:
        durations[number] += duration

    return durations



def compute_longest_time(calls):
    
    total_durations = {}

    for calling_number, receiving_number, _, duration in calls:
        total_durations = update_number(total_durations, calling_number, duration)
        total_durations = update_number(total_durations, receiving_number, duration)

    total_durations = list(total_durations.items())

    total_durations = sorted(total_durations, key=lambda x: x[1], reverse=True)
    longest_time_number = total_durations[0]

    return longest_time_number


if __name__ == "__main__":
    number, total_time = compute_longest_time(calls)
    print(f"{number} spent the longest time, {total_time} seconds, on the phone during September 2016.")


##########################################
# Tests
##########################################


def test_update_number():

    total_durations = {}
    number = "78130 00821"
    duration = "186"
    total_durations = update_number(total_durations, number, duration)
    assert total_durations[number] == 186

    number = "78130 00821"
    duration = "186"
    total_durations = update_number(total_durations, number, duration)
    assert total_durations[number] == 186 + 186

    print("Test update numbers ok!")





