import csv

"""
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""


def entries_retriever(filename):
    with open(filename, "r") as f:
        reader = csv.reader(f)  # O(n)
        entries = list(reader)  # O(n)
        return entries


def print_record_from_file(filename):
    entries = entries_retriever(filename)  # O(n)
    output = ""
    if len(entries) == 0:  # O(1)
        print(f"No data in the file {filename}")
        return
    if filename == "texts.csv":
        first_entry = entries[0]  # O(1)
        output = f"First record of texts, {first_entry[0]} texts {first_entry[1]} at time {first_entry[2]}"  # O(k), k length of the resulting string
    elif filename == "calls.csv":
        last_entry = entries[-1]  # O(1)
        output = f"Last record of calls, {last_entry[0]} calls {last_entry[1]} at time {last_entry[2]}, lasting {last_entry[3]} seconds"  # O(k), k length of the resulting string
    print(output)


print_record_from_file("texts.csv")  # O(n)
print_record_from_file("calls.csv")  # O(n)
