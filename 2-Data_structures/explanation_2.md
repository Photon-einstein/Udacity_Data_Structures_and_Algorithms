
## Reasoning Behind Decisions:
As the depth of the directory structure is not know in advance, a good strategy would be the recursion.  

For that an empty list was created, and then called the recursion function.  

Inside the recursion function, we get the list of possible directories from a given path, and them for each item, after concatenation with the parent path, we test if it is a directory, if yes, we perform another recursive call, if not, we test if the item is a file and it ends with the expected suffix, in the positive case, we add the item into the list.  

In the end of all the recursive calls we have an updated list with all the files with a given suffix.  

## Time Efficiency:
The time efficiency is the number of files and directories inside a given parent path, O(n).

## Space Efficiency:
The space efficiency is the number of matching files that have the expected suffix in their name, O(n).