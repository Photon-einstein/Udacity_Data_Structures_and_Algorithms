<!--
Problem 1: Square Root of an Integer

Provide an explanation for your answer, clearly organizing your thoughts into 
concise and easy-to-understand language.

Focus on explaining the reasoning behind your decisions rather than giving a 
detailed description of the code. For instance, why did you choose a particular 
data structure? Additionally, discuss the efficiency of your solution in terms 
of time and space complexity. If necessary, you can support your explanation 
with code snippets or mathematical formulas. For guidance on how to write 
formulas in markdown, refer to https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/writing-mathematical-expressions.
-->
The goal is to find the floored square root of a number, so the value would be  
the square root if that value is an integer or in case it is not, then it would  
be least integer that squared will be less than the value, and the next integer  
will be a bit larger than the original value.  
We can use binary search to get into the right value in $O(log \ n)$ time complexity,  
as each time there another recursion in the call stack the interval of values is halved  
half.

The space complexity is also $O(log \ n)$ as there will be $log \ n$ recursive calls in the  
worst case, each recursive call adds another call frame, apart from that inside each call  
stack the same space is always used, $O(1)$.

Conclusion:
* Time complexity: $O(log \ n)$  
* Space complexity: $O(log \ n)$
