'''
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Note:

Division between two integers should truncate toward zero.
The given RPN expression is always valid. That means the expression would always evaluate to a result and there won't be any divide by zero operation.
'''
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        calc = 0
        operators = {
          "+": (lambda a, b: a + b),
          "-": (lambda a, b: a - b),
          "*": (lambda a, b: a * b),
          "/": (lambda a, b: int(operator.truediv(a, b)))
        }
        output = []
        for i in tokens:
            if i in operators:
                b = output.pop()
                a = output.pop()
                result = (operators[i](a,b))
                output.append(int(result))
            else:
                output.append(int(i))
        return output.pop()
                
