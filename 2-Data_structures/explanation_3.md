
## Reasoning Behind Decisions:
I choose a min heap to handle the build of the huffman tree, so that  
the sorting of the nodes according to their frequency could be done in  
the most effective way automatically every time there was a push or a  
pop of a node from the tree.

## Time Efficiency:
The time efficiency of this solution is $O(n.log \ n)$, as for every character  
it must be inserted/retrieved from in the min heap, and every time this happens,  
the finding of the new minimum takes $O(n.log \ n)$.  

## Space Efficiency:
The space efficiency of this solution is $O(n)$ as for every different character  
that needs to be encoded there will be a need to create a new node in the min heap.  

