class Solution:


    def performOperation(self, operand1: int, operand2: int, token: str) -> int: 
        if token == '+': 
            return operand1 + operand2
        elif token == '-': 
            return operand1 - operand2
        elif token == '*': 
            return operand1 * operand2
        else:
            quotient = abs(operand1) // abs(operand2)

            if (operand1 < 0) != (operand2 < 0):
                return -quotient
            return quotient

    def evalRPN(self, tokens: List[str]) -> int:
        operandStack = []
        operators = {'+', '-', '*', '/'}
        for token in tokens: 
            if token not in operators: 
                operandStack.append(int(token))

            else: 
                operand2 = operandStack.pop()
                operand1 = operandStack.pop()
                res = self.performOperation(operand1, operand2, token)
                operandStack.append(res)
        return operandStack.pop()