


## A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self, handler=None):
        # Initialize the node with children as before, plus a handler
        self.children = {}
        self.handler = handler

    def set_handler(self, handler):
        self.handler = handler

    def __repr__(self):
        return f"RouteTrieNode({self.handler})"



## A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, handler):
        # Initialize the trie with a root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode(handler)

    def insert(self, path_parts, handler):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path

        node = self.root

        for path_part in path_parts:
            if path_part not in node.children:
                node.children[path_part] = RouteTrieNode()
            node = node.children[path_part]

        node.set_handler(handler)


    def find(self, path_parts):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match

        node = self.root
        if len(path_parts) == 1:
            return node.handler

        for path_part in path_parts:
            if path_part not in node.children:
                return
            node = node.children[path_part]

        return node.handler



## The Router class will wrap the Trie and handle
class Router:
    def __init__(self, handler, not_found_handler):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.routes = RouteTrie(handler)
        self.not_found_handler = not_found_handler

    def add_handler(self, path, handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        path_parts = self.split_path(path)
        self.routes.insert(path_parts, handler)

    def lookup(self, path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler

        path_parts = self.split_path(path)
        handler = self.routes.find(path_parts)

        if handler is None:
            handler = self.not_found_handler

        return handler

    def split_path(self, path):
        # you need to split the path into parts for
        # both the add_handler and loopup functions,
        # so it should be placed in a function here
        path_parts = path.split("/")
        path_parts = ["/"] + [part for part in path_parts if part != ""]
        return path_parts


def test():
    ## Here are some test cases and expected outputs you can use to test your implementation

    ## create the router and add a route
    router = Router("root handler", "not found handler") # remove the 'not found handler' if you did not implement this
    router.add_handler("/home/about", "about handler")  # add a route


    ## some lookups with the expected output
    assert router.lookup("/") == "root handler"
    assert router.lookup("/home/about") == "about handler"
    assert router.lookup("/home/about/") == "about handler"
    assert router.lookup("/home/about/me") == "not found handler"


if __name__ == "__main__":
    test()