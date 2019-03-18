
# the node class that will make up the binary tree


class Node:

    # initialise the class with a value and an empty left and right node
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # adds a node to this tree
    # in case this node already has a child on the correct branch,
    # this method becomes recursive and defers the task to its child nodes
    def addNode(self, value):
        #   RULE:
        # left =< value < right

        # if the new value is greater than the value in this node
        # we must store the new value in the right node
        if self.value < value:
            # if the right node is empty then create a new node with the value
            if self.right == None:
                self.right = Node(value)
            # if the right node contains some value then defer this task to that node
            else:
                self.right.addNode(value)
        # if the value is smaller than (or equal to this node)
        # it should be added to the left of this node
        else:
            # similarly if there is not left node, add a new one
            if self.left == None:
                self.left = Node(value)
            # if there already exists a left node then defer this task to that node
            else:
                self.left.addNode(value)

    # displays this node and all it's children 
    # spacing is used to add depth to the tree, the default is 0 so that the root node
    # has no indentation, by adding one to the spacing variable one \t is added before
    # each print
    def display(self, spacing = 0):
        # if this is the root then print that
        if spacing == 0:
            print("----ROOT----")
        # first print the actual value
        print("\t" * spacing, self.value)
        
        # print the left node (if it exists)
        if self.left != None:
            print("\t" * (spacing + 1), "----LEFT---->")
            self.left.display(spacing + 1)

        # print the right node (if it exists)
        if self.right != None:
            print("\t" * (spacing + 1), "----RIGHT---->")
            self.right.display(spacing + 1)

# create the root node variable and the user input varaible
num = 0
root = None

num = float(input("input the first (root) number: "))
# create the root node
root = Node(num)
# display for the first time
root.display()

# noe repeatedly accept more numbers
while True:
    # get input
    num = float(input("input the next number: "))

    # until the user enters -1
    if num == -1:
        break
    # if the user didnt enter -1 then add the value to the tree
    # and then display the tree
    else:
        print("\n\n\n")
        root.addNode(num)
        root.display()
    
print("finished")
print("the final binary tree is")
root.display()