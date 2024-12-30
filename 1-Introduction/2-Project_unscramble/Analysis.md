## Task0

**Description:** The problem involves reading two files and then printing the first record of texts and the last record of calls.

**Approach:** Read both files and then accessing directly the required data and printing it.

**Complexity Analysis**:
- **Algorithm**: Read the data from the two files and directly access the required data.
- **Big O Notation**: $O(n)$ where $n$ is the number of elements in the files
- **Justification**: Data access involves $O(1)$ time complexity to access the required data to print.  
String concatenation involves $O(k)$ where k is the length of the resulting string.  
So the lengthier operation will be reading the two files, row by row in $O(n)$ time complexity.

## Task1

**Description:** The problem involves calculating how many telephone numbers are in the records.

**Approach:** Read both files and then store the different calling and receiving numbers in a set to avoid number duplication.

**Complexity Analysis**:
- **Algorithm**: Read the data from the two files and store the numbers in a set to avoid numbers duplication
- **Big O Notation**: $O(n)$ where $n$ is the number of elements in the files
- **Justification**: Iterating throw each row of the files is the most lengthy operation $O(n)$.  
The other operations run in $O(1)$ time complexity.

## Task2

**Description:** The problem involves calculating the number with the longest duration of time spent on calls.

**Approach:** Read the data from the calls file, then store the cumulative duration of minutes in a call in a dictionary, both calling and receiving.  
Only after the calling and receiving updates of the dictionary are done will the result be completely calculated, with the result being updated on the fly.

**Complexity Analysis**:
- **Algorithm**: Store the cumulative duration of the calls for each number in a dictionary, and update the result on the fly.
- **Big O Notation**: $O(n)$ where $n$ is the number of elements in the files
- **Justification**: Iterating throw each row of the files is the most lengthy operation $O(n)$.  
The other operations run in $O(1)$ time complexity.

## Task3

**Description:** The problem involves getting all the prefix from the numbers that were called from a (080) Bangalore prefix, and print the list of codes one per line in lexicographic order with no duplicates.  
Perform the calculation of the percentage of calls from fixed lines in Bangalore that were made to fixed lines also in Bangalore.  
**Approach:** Store of the frequency of that prefix was done to a dictionary, then a sort to print the number and then a print of the ratio of the incoming calls also to Bangalore from the entire sample of starting calls from Bangalore.  

**Complexity Analysis**:
- **Algorithm**: Store the required data in a dictionary, sort the data, print the numbers, and then perform the calculation required to get the percentage.  
- **Big O Notation**: $O(n.log \ n)$ was the most expensive operation, performed during the sorting of the dictionary.  
- **Justification**:  The other operation were looping throw the rows of the file in $O(n)$ or constant time operations $O(1)$.

## Task4

**Description:** The telephone company want to identify numbers that might be doing telephone marketing.  
It was asked to create a set of possible telemarketers:  
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.  
The list of numbers should be print out one per line in lexicographic order with no duplicates.  
**Approach:** Get the set of possible candidates from the callers, and get the set of the exclusion list from the receivers of the calls and the numbers involved in the text exchange, then perform a set difference to trim the list of candidates getting rid of the exclusions.  
Then sort the set and print the final result.

**Complexity Analysis**:
- **Algorithm**: Set difference between the list of candidates and the list of numbers to exclude. Then sort the candidates and print the result.
- **Big O Notation**: $O(n.log \ n)$ was the most expensive operation, performed during the sorting of the dictionary.  
- **Justification**:  The other operations were looping throw the rows of the files in $O(n)$ or constant time operations $O(1)$.
