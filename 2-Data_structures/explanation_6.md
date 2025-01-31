
## Union Function

### Reasoning Behind Decisions:
I choose to store the values of the two lists in a single OrderedSet,  
so that I could get the unique values present in the two linked  
lists without repetitions. From the set I can get the unique ordered  
values into a single linked list.

### Time Efficiency:
The time efficiency of this solution is $O(n1 + n2)$ where n1 and n2  
are the sizes of the linked list 1 and 2 respectively.

### Space Efficiency:
The space efficiency if this solution of this solution is $O(n1 + n2)$  
where n1 and n2  are the sizes of the linked list 1 and 2 respectively    
considering the worst case scenario of all the elements in each list  
being unique.

## Intersection Function

### Reasoning Behind Decisions:
For the intersection function I choose to add the values of each  
list into a set, and then perform a set intersection and retrieve the  
values storing those into a new linked list.

### Time Efficiency:
The time efficiency of this solution is $O(n1 + n2)$ where n1 and  
n2 are the size of the linked lists 1 and 2.

### Space Efficiency:
The space efficiency of this solution is $O(n1 + n2)$ where n1 and  
n2 are the size of the linked lists 1 and 2, considering the worst  
case scenario of all the elements being unique.
