"""
Problem 7: Request Routing in a Web Server with a Trie

This module implements an HTTPRouter using a Trie data structure.

The HTTPRouter takes a URL path like "/", "/about", or 
"/blog/2019-01-15/my-awesome-blog-post" and determines the appropriate handler 
to return. The Trie is used to efficiently store and retrieve handlers based on 
the parts of the path separated by slashes ("/").

The RouteTrie stores handlers under path parts, and the Router delegates adding 
and looking up handlers to the RouteTrie. The Router also includes a not found 
handler for paths that are not found in the Trie and handles trailing slashes 
to ensure requests for '/about' and '/about/' are treated the same.

You should implement the function bodies the function signatures. Use the test 
cases provided below to verify that your algorithm is correct. If necessary, 
add additional test cases to verify that your algorithm works correctly.
"""

from typing import Optional


class RouteTrieNode:
    """
    A node in the RouteTrie, representing a part of a route.

    Attributes:
    children (dict): A dictionary mapping part of the route to the corresponding RouteTrieNode.
    handler (Optional[str]): The handler associated with this node, if any.
    """

    def __init__(self):
        """
        Initialize a RouteTrieNode with an empty dictionary for children and no handler.
        """
        self.children = dict()
        self.handler: Optional[str] = None


class RouteTrie:
    """
    A trie (prefix tree) for storing routes and their handlers.

    Attributes:
    root (RouteTrieNode): The root node of the trie.
    """

    def __init__(self, root_handler: str):
        """
        Initialize the RouteTrie with a root handler.

        Args:
        root_handler (str): The handler for the root node.
        """
        self.root: RouteTrieNode = RouteTrieNode()
        self.root.handler = root_handler

    def insert(self, path_parts: list[str], handler: str) -> None:
        """
        Insert a route and its handler into the trie.

        Args:
        path_parts (list[str]): A list of parts of the route.
        handler (str): The handler for the route.
        """
        trienode = self.root
        for i in range(len(path_parts)):
            path = path_parts[i]
            if path not in trienode.children.keys():
                trienode.children[path] = RouteTrieNode()
            if i == len(path_parts) - 1:
                trienode.children[path].handler = handler
            trienode = trienode.children[path]

    def find(self, path_parts: list[str]) -> Optional[str]:
        """
        Find the handler for a given route.

        Args:
        path_parts (list[str]): A list of parts of the route.

        Returns:
        str or None: The handler for the route if found, otherwise None.
        """
        node = self.root
        for path in path_parts:
            if path in node.children.keys():
                node = node.children[path]
            else:
                return None
        handler_route = node.handler
        return handler_route


class Router:
    """
    A router to manage routes and their handlers using a RouteTrie.

    Attributes:
    route_trie (RouteTrie): The trie used to store routes and handlers.
    not_found_handler (str): The handler to return when a route is not found.
    """

    def __init__(self, root_handler: str, not_found_handler: str):
        """
        Initialize the Router with a root handler and a not-found handler.

        Args:
        root_handler (str): The handler for the root route.
        not_found_handler (str): The handler for routes that are not found.
        """
        self.root_handler = root_handler
        self.not_found_handler = not_found_handler
        self.root = RouteTrie(self.root_handler)

    def clean_path(self, path: str) -> str:
        if path == "":
            path = "/"
        elif path[-1] == "/":
            path = path[:-1]
        return path

    def add_handler(self, path: str, handler: str) -> None:
        """
        Add a handler for a route.

        Args:
        path (str): The route path.
        handler (str): The handler for the route.
        """
        path_clean = self.clean_path(path)
        route_path = self.split_path(path_clean)
        self.root.insert(route_path, handler)

    def lookup(self, path: str) -> str:
        """
        Look up a route and return the associated handler.

        Args:
        path (str): The route path.

        Returns:
        str: The handler for the route if found, otherwise the not-found handler.
        """
        path_clean = self.clean_path(path)
        if path_clean == "/":
            return self.root_handler
        route_path = self.split_path(path_clean)
        handler = self.root.find(route_path)

        if handler == None:
            return self.not_found_handler
        else:
            return handler

    def split_path(self, path: str) -> list[str]:
        """
        Split the path into parts and remove empty parts to handle trailing slashes.

        Args:
            path (str): The path to split.

        Returns:
            List[str]: A list of parts of the path.
        """
        parts_bulk = path.split("/")
        parts = list()
        for el in parts_bulk:
            if el:
                parts.append(el)
        print(parts)
        return parts


if __name__ == "__main__":
    # create the router and add a route
    router = Router("root handler", "not found handler")
    router.add_handler("/home/about", "about handler")

    # Edge case: Empty path
    print("\nTest 1: Edge case empty path")
    handler = router.lookup("")
    print(handler)
    assert handler == "root handler"
    print("--------------------------------->Test 1 passed\n")
    # Expected output: 'Should print 'root handler'

    # Normal case: Path not found
    print("Test 2: Normal case path not found")
    handler = router.lookup("/home/contact")
    print(handler)
    assert handler == "not found handler"
    print("--------------------------------->Test 2 passed\n")
    # Expected output: 'not found handler'

    # Normal case: Path with multiple segments
    print("Test 3: Normal case path with multiple segments")
    handler = router.lookup("/home/about/me")
    print(handler)
    assert handler == "not found handler"
    print("--------------------------------->Test 3 passed\n")
    # Expected output: 'not found handler'

    # Normal case: Path with exact match
    print("Test 4: Path with exact match")
    handler = router.lookup("/home/about")
    print(handler)
    assert handler == "about handler"
    print("--------------------------------->Test 4 passed\n")
    # Expected output: 'about handler'

    # Edge case: Path not found
    print("Test 5: Edge case handler not found")
    handler = router.lookup("/home/")
    print(handler)
    assert handler == "not found handler"
    print("--------------------------------->Test 5 passed\n")
