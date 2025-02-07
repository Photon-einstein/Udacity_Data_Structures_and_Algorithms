<!--
Problem 5: Autocomplete with Tries

Provide an explanation for your answer, clearly organizing your thoughts into
concise and easy-to-understand language.

Focus on explaining the reasoning behind your decisions rather than giving a 
detailed description of the code. For instance, why did you choose a particular 
data structure? Additionally, discuss the efficiency of your solution in terms 
of time and space complexity. If necessary, you can support your explanation 
with code snippets or mathematical formulas. For guidance on how to write 
formulas in markdown, refer to https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/writing-mathematical-expressions.
-->

The TrieNode is composed each of 26 childs, each representing  
the letters of the alphabet, initially they are all None as  
there are no valid childs.

When there is one insert of a character in a given TrieNode,  
the child index corresponding to that given letter of the  
alphabet will now point to a valid TrieNode instead, recursively  
we will call insert again, now with a substring excluding the  
first character in each call, until all the characters are  
inserted, the time and space complexity of the insert method  
are thus $O(n)$ where n is the length of the string to insert.

The method suffixes of the TrieNode performs a depth first of  
the Trie, starting from the current node, it will collect  
recursively all the child nodes, bellow the current node.  
In terms of the time complexity, it will be $O(n)$, where n  
is the total number of characters bellow the current node.
In terms of space complexity it will also be $O(n)$ as there  
will be a storage of each character bellow the current node.  

The method insert of the Trie class performs an insert if a  
given word, starting from the root, it will iteratively  
traverse the word by each character, and starting from the  
root of the Trie, it will perform a check to see if the  
TrieNode already exist, if not it will create a new one  
and go one level deep in the tree, until all the characters  
are recorded in the tree. In terms of time complexity, it  
is $O(n)$ where n is the length of the new word to be  
inserted in the Trie. In terms of space complexity, in  
the worst case scenario, all the characters are not in  
the Trie, so it will be $O(n)$ where n is the length of  
the word to be inserted in the Trie.

The method find of the Trie will start in the root of the Trie,
and it will traverse each character in the prefix to be found,  
if all the characters are present in the right sequence,  
starting in the root then it will return the TrieNode of  
the last character, if the prefix is not present then it  
will return None. The time complexity is in the worst case  
scenario $O(n)$ where n is the length of the prefix.  
The space complexity is $O(1)$ as the same memory is used  
every time this method is executed.
