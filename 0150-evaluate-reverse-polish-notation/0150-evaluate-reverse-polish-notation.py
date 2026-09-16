class Solution(object):
    def evalRPN(self, tokens):
        stack = []

        for i in tokens:
            if i not in ['+', '-', '*', '/']:
                stack.append(int(i))
            else:
                b = stack.pop()
                a = stack.pop()

                if i == '+':
                    stack.append(a + b)

                elif i == '-':
                    stack.append(a - b)

                elif i == '*':
                    stack.append(a * b)

                else:
                    result = abs(a) // abs(b)

                    if (a < 0) != (b < 0):
                        result = -result

                    stack.append(result)

        return stack[-1]