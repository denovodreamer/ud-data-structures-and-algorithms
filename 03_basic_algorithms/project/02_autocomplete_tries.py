
class TrieNode:
    """
    A single node in the trie with children.
    """

    def __init__(self):
        self.is_word = False
        self.children = {}

    def insert(self, char):
        """
        Add a char to the children.
        """
        if char not in self.children:
            self.children[char] = TrieNode()
        return self.children[char]

    def get_words(self, node, suffix="", words=[]):
        """
        Get the suffixes of the current node.
        """
        child_nodes = node.children

        if len(child_nodes) == 0:
            words.append(suffix)
            return words

        for char in child_nodes:
            new_suffix = suffix + char
            node = child_nodes[char]
            words = self.get_words(node, new_suffix, words)

        return words

    def suffixes(self, suffix=""):
        """
        Search for all the suffixes starting in the current node.
        """

        complete_words = []

        node = self

        for char in suffix:
            child_nodes = node.children
            if char not in child_nodes:
                return

            node = node.children[char]

        if node.is_word:
            complete_words.append(suffix)

        complete_words = self.get_words(node, suffix, complete_words)

        return complete_words


class Trie:
    """
    Trie class with it's root node.
    """
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        Add a new word to the trie.
        """

        node = self.root

        for char in word:
            node = node.insert(char)

        node.is_word = True

    def find(self, prefix):
        """
        Locate the trie node corresponding to this prefix.
        """
        node = self.root

        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]

        return node



if __name__ == "__main__":
    word_list = [
        'apple',
        'bear',
        'goo',
        'good',
        'goodbye',
        'goods',
        'goodwill',
        'gooses',
        'zebra'
    ]
    trie = Trie()

    for word in word_list:
        trie.insert(word)


    prefix = "good"
    node = trie.find(prefix)
    print(list(node.children.keys()))
    if node:
        words = node.suffixes()
        print('\n'.join(words))
    else:
        print(prefix + " not found")