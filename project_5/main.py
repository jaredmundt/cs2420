'''
Project: 5
Author: Jared Mundt 
Course: cs2420
Date: 11/8/22

Description: 

Lessons Learned:

'''
from string import whitespace, punctuation
from bst import BST


class Pair:
    ''' Encapsulate letter,count pair as a single entity.

    Realtional methods make this object comparable
    using built-in operators. 
    '''

    def __init__(self, letter, count=1):
        self.letter = letter
        self.count = count

    def __eq__(self, other):
        return self.letter == other.letter

    def __hash__(self):
        return hash(self.letter)

    def __ne__(self, other):
        return self.letter != other.letter

    def __lt__(self, other):
        return self.letter < other.letter

    def __le__(self, other):
        return self.letter <= other.letter

    def __gt__(self, other):
        return self.letter > other.letter

    def __ge__(self, other):
        return self.letter >= other.letter

    def __repr__(self):
        return f'({self.letter}, {self.count})'

    def __str__(self):
        return f'({self.letter}, {self.count})'


def make_tree():
    ''' A helper function to build the tree.
    The test code depends on this function being available from main.
    :param: None
    :returns: A binary search tree
    '''
    tree = BST()
    with open('around-the-world-in-80-days-3.txt', 'r') as file:
        file = file.readlines()
        for line in file:
            for c in line:
                c = c.lower()
                if c not in whitespace and c not in punctuation:
                    try:
                        pair = tree.find(Pair(c))
                        pair.count += 1
                    except:
                        tree.add(Pair(c))

    return tree
                




def main():
    ''' Program kicks off here.

    '''
    make_tree()


if __name__ == "__main__":
    main()
