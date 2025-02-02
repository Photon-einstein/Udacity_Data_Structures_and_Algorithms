<!--
Problem 3: Rearrange Array Digits

Provide an explanation for your answer, clearly organizing your thoughts into
concise and easy-to-understand language.

Focus on explaining the reasoning behind your decisions rather than giving a 
detailed description of the code. For instance, why did you choose a particular 
data structure? Additionally, discuss the efficiency of your solution in terms 
of time and space complexity. If necessary, you can support your explanation 
with code snippets or mathematical formulas. For guidance on how to write 
formulas in markdown, refer to https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/writing-mathematical-expressions.
-->

As the sum has to be maximized, then larger digits should come first forming the two numbers.  
So we need to sort the array in descending order, we will need then to alternate the digits  
between the two numbers.

For the sorting algorithm I used the Mergesort as it has a time complexity of $O(n \ log \ n)$.  
In the end the two list are converted into numbers and the result is returned.  

Time complexity: The solution uses merge sort that has a time complexity of $O(n \ log \ n)$,  
after the sorting the method calculate_tuple_element_value has a time complexity of $O(n)$ as  
it iterates over the array.  

Space complexity: The space complexity of the Mergesort is $O(n)$ because of the temporary  
lists that are created during the method. The method calculate_tuple_element_value uses the  
same amount of memory, $O(1)$, so this solution is dominated by the space requirements of  
the Mergesort.  

**Conclusion**:
* Time complexity: $O(n \ log \ n)$  
* Space complexity: $O(n)$