"""
DESCRIPTION:


Your job is to create a calculator which evaluates expressions in Reverse Polish notation.

For example expression 5 1 2 + 4 * + 3 - (which is equivalent to 5 + ((1 + 2) * 4) - 3 in normal notation) should evaluate to 14.

Note that for simplicity you may assume that there are always spaces between numbers and operations, e.g. 1 3 + expression is valid, but 1 3+ isn't.

Empty expression should evaluate to 0.

Valid operations are +, -, *, /.

You may assume that there won't be exceptional situations (like stack underflow or division by zero).
"""


def calc(expr):
    nums = [0]

    for item in expr.split():
        try:
            nums.append(float(item))
        except ValueError:
            nums.append(_operation(nums.pop(), nums.pop(), item))
    return nums.pop()


def _operation(n, m, op):
    switch = {
        '+': '__add__',
        '-': '__sub__',
        '*': '__mul__',
        '/': '__truediv__',
    }
    return getattr(m, switch[op])(n)


"""
BEST SOLUTION:


import operator

def calc(expr):
    OPERATORS = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
    stack = [0]
    for token in expr.split():
        if token in OPERATORS:
            op2, op1 = stack.pop(), stack.pop()
            stack.append(OPERATORS[token](op1,op2))
        elif token:
            stack.append(float(token))
    return stack.pop()

-------------------------------------------------------------------------------

operator = set(['+', '-', '*', '/'])

def calc(expr):
    stack = list()
    for c in expr.split():
      if c in operator :
          first = stack.pop()
          second = stack.pop()
          stack.append(str(eval(second + c + first)))
        else : stack.append(c)
    return eval(stack.pop()) if stack else 0
"""
