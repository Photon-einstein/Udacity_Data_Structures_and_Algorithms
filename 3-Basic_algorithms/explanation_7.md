<!--
Problem 7: Request Routing in a Web Server with a Trie

Provide an explanation for your answer, clearly organizing your thoughts into 
concise and easy-to-understand language.

Focus on explaining the reasoning behind your decisions rather than giving a 
detailed description of the code. For instance, why did you choose a particular 
data structure? Additionally, discuss the efficiency of your solution in terms 
of time and space complexity. If necessary, you can support your explanation 
with code snippets or mathematical formulas. For guidance on how to write 
formulas in markdown, refer to https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/writing-mathematical-expressions.
-->

In the Router class, in the method add_handler, I first cleaned the path, to  
avoid trailing '/' characters, then I split the path by the '/' characters,  
and after that I inserted into the root, being the root a RouteTrie node.   
The time complexity is dominated by the call to split_path and insert, each   
with $O(n)$ time complexity. The space complexity is also $O(n)$ where n will  
be each part of the path.

In the method lookup of the Router class, I also cleaned first the path, then  
split using the '/' character and then called the find method from the root of  
the Router class, returning the handler as the final result. The time complexity  
of this method is dominated by the split_path and the call of find in the root,  
with a complexity of $O(n)$. The space complexity is $O(n)$ where n are the number  
of parts in a given path.  
 
The split_path from the Router class splits the path using the character '/',  
appending the result into a list. The time complexity is $O(n)$, where n are the  
number of parts in a given path, the space complexity is also $O(n)$ as each part  
of the path has to be saved.

The class RouteTrie has as the root a RouteTrieNode, so that it enables it to store  
the children in a dictionary, enabling it to add new nodes in O(1) time complexity. 

The insert method of the RouteTrie class, starts the search at the RouteTrieNode  
root, traverses the list of path parts, and if the part is still not at the  
RouteTrieNode children dictionary, it will add it. When we reach the last part of  
the path, the handler will be also inserted into the RouteTrieNode. At each cycle   
there is a traversal in the tree into the next node. The time complexity of the  
insert method is $O(n)$ as there is a traversal of a list of parts, the space  
complexity is $O(1)$, as the same memory is always used.  

The find method of the class RouteTrie will start at the RouteTrieNode root,  
and perform a traversal check for each part of the path, testing if each part is  
present at each node, if yes then it will continue the traversal of the tree until  
the last part is reached and the handler of the route is accessible. The time  
complexity of the find method is $O(n)$ as there is a traversal of a list of parts,  
the space complexity is $O(1)$, as the same memory is always used.  
