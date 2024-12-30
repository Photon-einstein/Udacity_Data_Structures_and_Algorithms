import csv

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""


def entries_retriever(filename):
    with open(filename, "r") as f:
        reader = csv.reader(f)  # O(n)
        entries = list(reader)  # O(n)
        return entries


def update_dictionary(
    d, entry, index, max_duration_call_count, max_duration_call_telephone_number
):
    if entry[index] in d:  # O(1)
        d[entry[index]] += int(entry[3])  # O(1)
    else:
        d[entry[index]] = int(entry[3])  # O(1)
    if int(d[entry[index]]) > max_duration_call_count:  # O(1)
        max_duration_call_count = int(d[entry[index]])  # O(1)
        max_duration_call_telephone_number = entry[index]  # O(1)
    return max_duration_call_telephone_number, max_duration_call_count


def retrieve_telephone_number_with_longest_cumulative_call(filename):
    max_duration_call_count = 0
    max_duration_call_telephone_number = ""
    d = dict()
    entries = entries_retriever(filename)  # O(n)
    for entry in entries:  # O(n)
        max_duration_call_telephone_number, max_duration_call_count = update_dictionary(
            d, entry, 0, max_duration_call_count, max_duration_call_telephone_number
        )  # O(1)
        max_duration_call_telephone_number, max_duration_call_count = update_dictionary(
            d, entry, 1, max_duration_call_count, max_duration_call_telephone_number
        )  # O(1)
    print(
        f"{max_duration_call_telephone_number} spent the longest time, {max_duration_call_count} seconds, on the phone during September 2016."
    )  # O(1)


filename = "calls.csv"
retrieve_telephone_number_with_longest_cumulative_call(filename)  # O()
