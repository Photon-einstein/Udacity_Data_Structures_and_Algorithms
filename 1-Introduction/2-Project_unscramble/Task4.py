import csv

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


def entries_retriever(filename):
    with open(filename, "r") as f:
        reader = csv.reader(f)  # O(n)
        entries = list(reader)  # O(n)
        return entries


def calculate_possible_telemarketers_numbers():
    calls_filename = "calls.csv"  # O(1)
    text_filename = "texts.csv"  # O(1)
    calls = entries_retriever(calls_filename)  # O(n)
    texts = entries_retriever(text_filename)  # O(n)
    # candidates initial calculation
    set_possible_candidates = set()  # O(1)
    set_receive_incoming_calls_exclusion = set()  # O(1)
    for call in calls:  # O(n)
        set_possible_candidates.add(call[0])  # O(1)
        set_receive_incoming_calls_exclusion.add(call[1])  # O(1)
    # send text exclusion set calculation
    set_send_receive_text_exclusion = set()  # O(1)
    for text in texts:
        set_send_receive_text_exclusion.add(text[0])  # O(1)
        set_send_receive_text_exclusion.add(text[1])  # O(1)
    # calculation candidates
    set_possible_candidates -= (
        set_receive_incoming_calls_exclusion | set_send_receive_text_exclusion
    )  # O(n)
    list_possible_candidates = list(set_possible_candidates)  # O(n)
    list_possible_candidates.sort()  # O(n. log n)
    print("These numbers could be telemarketers: ")  # O(1)
    for possible_candidate in list_possible_candidates:  # O(n)
        print(possible_candidate)  # O(1)


calculate_possible_telemarketers_numbers()  # O(n. log n)
