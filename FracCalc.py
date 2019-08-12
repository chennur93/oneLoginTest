from fractions import Fraction

class Calc:

    def __init__(self, input):
        self.input = input

    def calculate(self, op, a, b):
        """
        Computes the operation and returns the result.

        Parameters:
            op: operator
            a: operand
            b: operand

        Returns:
            Result of the operation.
        """
        if op == "+":
            return a + b
        elif op == "-":
            return a - b
        elif op == "*":
            return a * b
        elif op == "/":
            return a / b

    def getFrac(self, frac):
        """
        method to get fraction from a mixed fraction string of type a_b/c

        Parameters:
            frac: fraction of string type or instance of Fraction.

        Returns:
            a Fraction value.
        """
        if isinstance(frac, Fraction):
            return frac
        elif "_" in frac:
            temp = frac.split("_")
            num = (Fraction(temp[0])*Fraction(temp[1]).denominator)+ \
            Fraction(temp[1]).numerator
            denom = Fraction(temp[1]).denominator
            return Fraction(num, denom)
        else:
            return Fraction(frac)

    def getResult(self):
        """
        Computes the result of a given expression.

        Returns:
            Result in the form of a fraction or integer. 
        """
        temp = self.input.split()
        operands = ['/', '*', '+', '-']
        i = 0

        if temp[0] == "?":
            temp = temp[1:]

        while i < len(operands):
            if len(temp) == 1:
                val = self.getFrac(temp[0])
                if val.numerator > val.denominator and val.denominator != 1:
                    return "= " + str(val.numerator // val.denominator) + \
                    "_" + str(val.numerator % val.denominator) + "/" + \
                    str(val.denominator)
                else:
                    return "= " + str(val)
            else:
                if operands[i] in temp:
                    op_index = temp.index(operands[i])
                    operand_one = self.getFrac(temp[op_index - 1])
                    operand_two = self.getFrac(temp[op_index + 1])
                    val = self.calculate(operands[i], operand_one, operand_two)
                    temp[op_index-1] = val
                    temp.remove(temp[op_index])
                    temp.remove(temp[op_index])
                else:
                    i += 1
