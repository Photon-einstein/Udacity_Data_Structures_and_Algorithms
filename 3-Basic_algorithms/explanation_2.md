<!--
Problem 2: Search in a Rotated Sorted Array

Provide an explanation for your answer, clearly organizing your thoughts into 
concise and easy-to-understand language.

Focus on explaining the reasoning behind your decisions rather than giving a 
detailed description of the code. For instance, why did you choose a particular 
data structure? Additionally, discuss the efficiency of your solution in terms 
of time and space complexity. If necessary, you can support your explanation 
with code snippets or mathematical formulas. For guidance on how to write 
formulas in markdown, refer to https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/writing-mathematical-expressions.
-->
If there was no rotation, the array would be sorted in ascending order.  
As we have a rotation in the array, it means that we will have two  
ascending order arrays, there are different scenarios in our binary search:

1. The interval where we are search is not rotated and the sub array is sorted  
in ascending order, in that case we can use normally the binary search to search the given value.

2. The interval is rotated witch means that numbers inside are not sorted in  
ascending order, so we have to continue our binary search until the sub array is sorted,  
then we can decide if the value was found or not.

We can use binary search to get into the right value in $O(log \ n)$ time complexity,  
as each time there another recursion in the call stack the interval of values is halved  
half.

The space complexity is also $O(log \ n)$ as there will be $log \ n$ recursive calls in the  
worst case, each recursive call adds another call frame, apart from that inside each call  
stack the same space is always used, $O(1)$.

Conclusion:
* Time complexity: $O(log \ n)$  
* Space complexity: $O(log \ n)$