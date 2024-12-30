import csv

"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""


def entries_retriever(filename):
    with open(filename, "r") as f:
        reader = csv.reader(f)  # O(n)
        entries = list(reader)  # O(n)
        return entries


def count_telephone_numbers(list_files):
    count = 0
    s = set()  # O(1)
    for file in list_files:  # O(m)
        entries = entries_retriever(file)  # O(n)
        for entry in entries:  # O(n)
            s.add(entry[0])  # O(1)
            s.add(entry[1])  # O(1)
    count = len(s)  # O(1)
    print(f"There are {count} different telephone numbers in the records.")


list_files = ["texts.csv", "calls.csv"]
count_telephone_numbers(list_files)  # O(n)
