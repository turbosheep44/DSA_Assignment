
import io
import sys

# create a dictionary of allowed operators
# each with a lambda function to perform that operation 
operations = {
  "+": (lambda x, y: x + y),
  "-": (lambda x, y: y - x),
  "*": (lambda x, y: x * y),
  "/": (lambda x, y: y / x),
  # added power operator because the examples of RPN found 
  # online and used to test had powers
  "^": (lambda x, y: y ** x)
}

# wrapper for parseExpression which gets all the print outputs and redirects them to a string which
# is returned 
# see question 7 Node.getDisplayString for a similar use case
def parseExpressionStringOutput(expression):
    output = io.StringIO()
    parseExpression(expression, output)
    return output.getvalue()

def parseExpression(expression, outputStream = sys.stdout):
    # remove any trailing spaces
    expression = expression.strip()

    # there should be a space between each literal in the experssion so
    # split the string based on the spaces 
    expressionLiterals = expression.split(" ")

    # declare this variable before the loop so that is is not declared 
    # with each iteration of the loop
    n = None
    # also declare the stack as an empty list
    stack = []

    # repeat this part while there are still items in the expression
    while len(expressionLiterals) != 0:
        # print the contents of the stack
        print("Stack contents:", file=outputStream)
        print("\t", stack, file=outputStream)    

        # take the next item from the list of literals
        n = expressionLiterals.pop(0)
        # output the literaly we are about to process
        print("\n\tprocessing now: ", n, file=outputStream)

        # if this is one of the allowed operations
        if n in operations:
            # pop two variables from the stack and
            # use the lambda function from the dictionary
            result = operations[n](stack.pop(), stack.pop())
            # then push the result
            stack.append(result)
            print("\tperform operation {", n, "} push to stack {", result, "}", file=outputStream)
        else:
            # if the next literal is not an operation then push it onto the stack
            # also cast it to a number so that when it is eventally pulled from
            # the stack to be used for some operation it is already numerical
            stack.append(float(n))
            print("\tpush to stack", file=outputStream)

        #print a new line for readability
        print("", file=outputStream)

    # once the whole expression has been evaluated the only remaining item on the stack
    # will be the result
    print("Result >> ", stack.pop(), file=outputStream)
    #if there is still something on the stack then something went wrong
    if len(stack) != 0:
        print("Oh no! It looks like something went wrong. The stack still contains these values:", stack, file=outputStream)


if __name__ == '__main__':
    # test case 
    expression = "9 5 3 + 2 4 ^ - +"
    print()
    print(expression)
    parseExpression(expression)
    print()
