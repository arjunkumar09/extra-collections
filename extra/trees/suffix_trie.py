"""
Suffix trees store information about a single string and exports a huge amount
of structural information about that string.
"""
from abc import abstractmethod
from extra.interface import Extra
from extra.trees.radix_trie import RadixTrie



class SuffixTrie(Extra):

    def __init__(self, word):
        assert type(word) == str, "The initial value must be a string!!"
        assert len(word) > 0, "An empty string can't be used!!"
        # Ukkonen's algorithm
        self._rt = RadixTrie()
        for idx in range(len(word)):
            self._rt.insert(word[idx:])

    @abstractmethod
    def from_iterable(self, iterable):
        #TODO:
        pass


    def __repr__(self):
        return str(self._rt)


    def __len__(self):
        return len(self._rt)


    def has_suffix(self, suffix):
        return self._rt.has_prefix(suffix)


    def has_substr(self, substr):
        return self._rt.has_prefix(substr)


    def get_lcs(self):
        #TODO:stands for "Longest Common Substring"
        pass


    def get_lrs(self):
        """TODO
        LRS stands for "Longest Repeated Substring". lrs is the longest
        substring that occurs at least twice.
        """
        pass


    def get_longest_palindrome(self):
        #TODO
        pass


    def get_lowest_common_ancestor(self):
        #TODO
        pass
    

    def to_suffix_array(self):
        #TODO
        pass








if __name__ == "__main__":
    # st = SuffixTrie("banana")
    # print(st)
    # print(st.has_substr('nan'))
    
    # st = SuffixTrie("ATCGATCGA")
    # print(st)
    # # print(st.get_longest_repeated_substr())
    # print("Total Nodes:", len(st))


    # st = SuffixTrie("minimize")
    # print(st)
    # print("Total Nodes:", len(st))
    # print(st.has_suffix('ize'))    

    # st = SuffixTrie("nonsense")
    # print(st)
    # print("Total Nodes:", len(st))
    # print(st.has_substr("se"))
    # print(st.get_lrs())


    st = SuffixTrie("ABABABA")
    print(st)
    print(st.get_lrs())    

