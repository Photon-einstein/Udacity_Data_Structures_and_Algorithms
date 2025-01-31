
## Reasoning Behind Decisions:
I used a stack to check if a user is present some group or  
sub-group, after checking the present group, the sub-groups  
belonging to that group are added to the stack, and then the  
search continues iteratively while there are sub groups to be  
checked.

## Time Efficiency:
The time efficiency is $O(n * u)$ as all the groups and sub-groups  
n have to be visited and then a search has to be made to each list  
of u users.

## Space Efficiency:
The space efficiency of this solution is $O(n)$ as all the group and  
sub-groups have to be saved in the stack in the worst case scenario  
if they are all subgroups of a single parent group.
