<!--
Problem 6: Unsorted Integer Array

Provide an explanation for your answer, clearly organizing your thoughts into
concise and easy-to-understand language.

Focus on explaining the reasoning behind your decisions rather than giving a 
detailed description of the code. For instance, why did you choose a particular 
data structure? Additionally, discuss the efficiency of your solution in terms 
of time and space complexity. If necessary, you can support your explanation 
with code snippets or mathematical formulas. For guidance on how to write 
formulas in markdown, refer to https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/writing-mathematical-expressions.
-->
This solution will in one single list traversal, check if each element  
is greater than the current maximum or less that the current minimum,  
if yes then the values will be updated. The first value of the list  
initializes the min and max values.
The time complexity of this solution is thus $O(n)$ where n is the  
length of the list. The space complexity of this solution is $O(1)$  
as the same memory is always used, independent of the length of the list.
