from typing import Optional


class Node:
    """
    A class to represent a node in a linked list.

    Attributes:
    -----------
    value : int
        The value stored in the node.
    next : Optional[Node]
        The reference to the next node in the linked list.
    """

    def __init__(self, value: int) -> None:
        """
        Constructs all the necessary attributes for the Node object.

        Parameters:
        -----------
        value : int
            The value to be stored in the node.
        """
        self.value: int = value
        self.next: Optional[Node] = None

    def __repr__(self) -> str:
        """
        Return a string representation of the node.

        Returns:
        --------
        str
            A string representation of the node's value.
        """
        return str(self.value)


class LinkedList:
    """
    A class to represent a singly linked list.

    Attributes:
    -----------
    head : Optional[Node]
        The head node of the linked list.
    """

    def __init__(self) -> None:
        """
        Constructs all the necessary attributes for the LinkedList object.
        """
        self.head: Optional[Node] = None

    def __str__(self) -> str:
        """
        Return a string representation of the linked list.

        Returns:
        --------
        str
            A string representation of the linked list, with nodes separated by " -> ".
        """
        cur_head: Optional[Node] = self.head
        out_string: str = ""
        while cur_head:
            out_string += str(cur_head.value)
            if cur_head.next:
                out_string += " -> "
            cur_head = cur_head.next
        return out_string

    def append(self, value: int) -> None:
        """
        Append a new node with the given value to the end of the linked list.

        Parameters:
        -----------
        value : int
            The value to be stored in the new node.
        """
        if self.head is None:
            self.head = Node(value)
            return

        node: Node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self) -> int:
        """
        Calculate the size (number of nodes) of the linked list.

        Returns:
        --------
        int
            The number of nodes in the linked list.
        """
        size: int = 0
        node: Optional[Node] = self.head
        while node:
            size += 1
            node = node.next

        return size


def union(llist_1: LinkedList, llist_2: LinkedList) -> LinkedList:
    """
    Compute the union of two linked lists.

    Parameters:
    -----------
    llist_1 : LinkedList
        The first linked list.
    llist_2 : LinkedList
        The second linked list.

    Returns:
    --------
    LinkedList
        A new linked list containing all unique elements from both input linked lists.
    """
    # Use a set to store all unique elements
    s = set()
    union_list = LinkedList()
    update_set(s, llist_1)
    update_set(s, llist_2)
    sorted_values = sorted(s)
    for value in sorted_values:
        union_list.append(value)
    return union_list


def intersection(llist_1: LinkedList, llist_2: LinkedList) -> LinkedList:
    """
    Compute the intersection of two linked lists.

    Parameters:
    -----------
    llist_1 : LinkedList
        The first linked list.
    llist_2 : LinkedList
        The second linked list.

    Returns:
    --------
    LinkedList
        A new linked list containing all elements that are present in both input linked lists.
    """
    s1 = set()
    s2 = set()
    intersection_list = LinkedList()
    update_set(s1, llist_1)
    update_set(s2, llist_2)
    sorted_values = sorted(s1 & s2)
    for value in sorted_values:
        intersection_list.append(value)
    return intersection_list


def update_set(s: set, llist: LinkedList) -> None:
    if llist is None:
        return
    node = llist.head
    while node:
        s.add(node.value)
        node = node.next


if __name__ == "__main__":
    ## Test case 1
    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()

    element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
    element_2 = [6, 32, 4, 9, 6, 1, 11, 21, 1]

    for i in element_1:
        linked_list_1.append(i)

    for i in element_2:
        linked_list_2.append(i)

    print("Test Case 1:")
    print(
        "Union:", union(linked_list_1, linked_list_2)
    )  # Expected: 1, 2, 3, 4, 6, 9, 11, 21, 32, 35, 65
    print(
        "Intersection:", intersection(linked_list_1, linked_list_2)
    )  # Expected: 4, 6, 21
    union_list = union(linked_list_1, linked_list_2)
    intersection_list = intersection(linked_list_1, linked_list_2)
    assert (
        union_list.__str__()
        == "1 -> 2 -> 3 -> 4 -> 6 -> 9 -> 11 -> 21 -> 32 -> 35 -> 65"
    )
    assert intersection_list.__str__() == "4 -> 6 -> 21"
    print("Test Case 1 passed")

    ## Test case 2
    linked_list_3 = LinkedList()
    linked_list_4 = LinkedList()

    element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]
    element_2 = [1, 7, 8, 9, 11, 21, 1]

    for i in element_1:
        linked_list_3.append(i)

    for i in element_2:
        linked_list_4.append(i)

    print("\nTest Case 2:")
    print(
        "Union:", union(linked_list_3, linked_list_4)
    )  # Expected: 1, 2, 3, 4, 6, 7, 8, 9, 11, 21, 23, 35, 65
    print(
        "Intersection:", intersection(linked_list_3, linked_list_4)
    )  # Expected: empty
    union_list = union(linked_list_3, linked_list_4)
    intersection_list = intersection(linked_list_3, linked_list_4)
    assert (
        union_list.__str__()
        == "1 -> 2 -> 3 -> 4 -> 6 -> 7 -> 8 -> 9 -> 11 -> 21 -> 23 -> 35 -> 65"
    )
    assert intersection_list.__str__() == ""
    print("Test Case 2 passed")

    ## Test case 3
    linked_list_5 = None
    linked_list_6 = LinkedList()

    element_1 = [1, 7, 8, 9, 11, 21, 1]
    for i in element_1:
        linked_list_6.append(i)

    print("\nTest Case 3:")
    print("Union:", union(linked_list_5, linked_list_6))  # Expected: 1, 7, 8, 9, 11, 21
    print(
        "Intersection:", intersection(linked_list_5, linked_list_6)
    )  # Expected: empty
    union_list = union(linked_list_5, linked_list_6)
    intersection_list = intersection(linked_list_5, linked_list_6)
    assert union_list.__str__() == "1 -> 7 -> 8 -> 9 -> 11 -> 21"
    assert intersection_list.__str__() == ""
    print("Test Case 3 passed")

    ## Test case 4
    linked_list_7 = None
    linked_list_8 = None

    print("\nTest Case 4:")
    print("Union:", union(linked_list_7, linked_list_8))  # Expected: Empty
    print(
        "Intersection:", intersection(linked_list_5, linked_list_6)
    )  # Expected: empty
    union_list = union(linked_list_7, linked_list_8)
    intersection_list = intersection(linked_list_7, linked_list_8)
    assert union_list.__str__() == ""
    assert intersection_list.__str__() == ""
    print("Test Case 4 passed")
