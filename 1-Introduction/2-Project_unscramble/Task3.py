import csv

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


def entries_retriever(filename):
    with open(filename, "r") as f:
        reader = csv.reader(f)  # O(n)
        entries = list(reader)  # O(n)
        return entries


def extract_prefix_helper(number, delimiter):
    prefix = ""
    for c in number:  # O(m)
        prefix += c  # O(1)
        if c == delimiter:
            break
    return prefix


def extract_prefix(number):
    if number[0] == "(":
        return extract_prefix_helper(number, ")")  # O(m)
    elif number[:3] == "140":
        return number[:3]  # O(1)
    elif number.startswith(("7", "8", "9")):
        return number[0:4]  # O(1)


def retrieve_all_area_codes_and_mobile_prefixes(filename):
    entries = entries_retriever(filename)  # O(n)
    d = dict()  # O(1)
    for entry in entries:  # O(n)
        if entry[0][:5] == "(080)":
            if extract_prefix(entry[1]) not in d:  # O(1)
                d[extract_prefix(entry[1])] = 1  # O(1)
            else:
                d[extract_prefix(entry[1])] += 1  # O(1)
    print("The numbers called by people in Bangalore have codes:")  # O(1)
    d = dict(sorted(d.items()))  # O(n.log n)
    size_dict = 0
    for key, value in d.items():  # O(n)
        print(key)  # O(1)
        size_dict += value  # O(1)
    return d, size_dict


def calculate_percentage_calls_in_bangalore(d, size_dict):
    bangalore_prefix = "(080)"  # O(1)
    count_bangalore_prefix = d[bangalore_prefix]  # O(1)
    percentage = count_bangalore_prefix / size_dict * 100  # O(1)
    print(
        f"\n{percentage:.2f} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore."
    )  # O(1)


# Part A
filename = "calls.csv"  # O(1)
d, size_dict = retrieve_all_area_codes_and_mobile_prefixes(filename)  # O(n.log n)

# Part B
calculate_percentage_calls_in_bangalore(d, size_dict)  # O(1)
