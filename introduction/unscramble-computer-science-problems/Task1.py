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
phone_numbers = []
for call in calls:
    if call[0] not in phone_numbers:
        phone_numbers.append(call[0])
    if call[1] not in phone_numbers:
        phone_numbers.append(call[1])

for text in texts:
    if text[0] not in phone_numbers:
        phone_numbers.append(text[0])
    if text[1] not in phone_numbers:
        phone_numbers.append(text[1])


print(f"There are {len(phone_numbers)} different telephone numbers in the records.")