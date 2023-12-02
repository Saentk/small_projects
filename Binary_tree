class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

# add method to create nodes
    def add(self, data):

        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.add(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.add(data)
        else:
            self.data = data


# findvalue method to compare the value with nodes
    def findvalue(self, work_val):
        if work_val < self.data:
            if self.left is None:
                return str(work_val)+" Not Found"
            return self.left.findvalue(work_val)
        elif work_val > self.data:
            if self.right is None:
                return str(work_val)+" Not Found"
            return self.right.findvalue(work_val)
        else:
            print(str(self.data) + ' is found')
# Print the tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.data),
        if self.right:
            self.right.PrintTree()


root = Node(12)
root.add(6)
root.add(14)
root.add(3)
print(root.findvalue(7))
print(root.findvalue(14))
