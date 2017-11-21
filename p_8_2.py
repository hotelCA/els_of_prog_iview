import re

class RPNEvaluator:
    numeric_pattern = re.compile('[-]?[0-9]+')

    @classmethod
    def evaluate_RPN(cls, RPN):
        # Mention about checking RPN validity
        lhs, rhs = RPN[0], RPN[1]
        for x in RPN[2:]:
            if cls.numeric_pattern.match(x):
                rhs = x
            else:
                lhs = cls.calculate(int(lhs), int(rhs), x)
        return lhs

    @classmethod
    def evaluate_RPN_recursively(cls, RPN):
        # Mention about checking validity of RPN
        return cls.evaluate(RPN[:-1], RPN[-1])

    @classmethod
    def evaluate(cls, RPN, operator):
        if len(RPN) == 2:
            return cls.calculate(int(RPN[0]), int(RPN[1]), operator)
        else:
            return cls.calculate(cls.evaluate(RPN[:-2], RPN[-2]), int(RPN[-1]), operator)

    @classmethod
    def calculate(cls, x, y, operator):
        if operator == '+':
            return x + y
        elif operator == '-':
            return x - y
        elif operator == '*':
            return x * y
        elif operator == '/':
            return x / y
        else:
            raise NotImplementedError('calculate(): Operator not implemented')


print(RPNEvaluator.evaluate_RPN_recursively(['-2','3','*','-5','+']))