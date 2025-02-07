<!--
Problem 4: Dutch National Flag Problem

Provide an explanation for your answer, clearly organizing your thoughts into
concise and easy-to-understand language.

Focus on explaining the reasoning behind your decisions rather than giving a 
detailed description of the code. For instance, why did you choose a particular 
data structure? Additionally, discuss the efficiency of your solution in terms 
of time and space complexity. If necessary, you can support your explanation 
with code snippets or mathematical formulas. For guidance on how to write 
formulas in markdown, refer to https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/writing-mathematical-expressions.
-->

The idea is to sort the 0's and the 2's, so that the 1's will  
be automatically sorted as well. The 0's and 2's have their  
own index of the last position to be placed, and a third index,  
front_index will go over the array, and when it's value at that  
index is 0, it will swap the value with the value present at the  
index for the value 0, after that the index for value 0 will be  
incremented.  

If the value at the front index is 2, then the value at index for  
the 2's will be swapped and the index for the 2's will be  
decremented, as we want the sorting to be done in ascending order.  

If the value at front index is 1, then there is no need to do a  
swap for 0's or 2's, and the front index needs only to be incremented.

This cycle continues until the front index is greater than the index  
of the 2's, as that implies that the array is already sorted in  
ascending order.  

The time complexity of this algorithm is $O(n)$ as there is only one  
cycle over the values present at the input list.  

The space complexity of this algorithm is $O(1)$ as the sorting of  
this algorithm is done in place, and no additional data structures  
are used that scale with the input size.  

**Conclusion**:
* Time complexity: $O(n)$  
* Space complexity: $O(1)$
