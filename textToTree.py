import sys


class Node:
    def __init__(self, word):
        self.word = word
        self.right = None
        self.left = None

    def printTree(self):

        print(self.word)

        if (self.left) :
            self.left.printTree()
        if (self.right):
            self.right.printTree()

    def insert(self,word):
        if self.word and self.word != "":
            if word < self.word:
                if self.left is None:
                    self.left = Node(word)
                else:
                    self.left.insert(word)
            elif word > self.word:
                if self.right is None:
                    self.right = Node(word)
                else:
                    self.right.insert(word)

        else:
            self.word = word



def main():
    file = sys.argv[1]
    line = ""
    words = []

    with open(file) as f:
        line = f.readline()
        words = line.split()
        print(words)

    root = Node(words[0])

    for word in words:
        root.insert(word)

    root.printTree()

if __name__ == "__main__":
    main()