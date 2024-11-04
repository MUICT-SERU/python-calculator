class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        result = 0
        is_negative = (a < 0) and (b < 0)  
        if is_negative is True:
            a, b = abs(a), abs(b) 
        for i in range(b):
            result = self.add(result, a)
        return result

    def divide(self, a, b):
       
        if b == 0:
            return "Cannot divide by zero"
        is_negative = (a < 0) ^ (b < 0)  
        a, b = abs(a), abs(b)
        result = 0
        while a >= b:
            a = self.subtract(a, b)
            result += 1
        if is_negative:
            return -result  
        else:
            return result


    def modulo(self, a, b):
        Back_b = b
        if b == 0:
            return "Cannot modulo by zero"
        is_negative = (a < 0) and (b < 0)  
        a, b = abs(a), abs(b)
        while a >= b:
            a = a-b
        if is_negative:
            return -a  
        else:
            if Back_b < 0:
                return -a
            else:
                return a
                

# Example usage:
if __name__ == "__main__":
    calc = Calculator()
    print("This is a simple calculator class!")
    print("Example: addition: ", calc.add(1, 2))
    print("Example: subtraction: ", calc.subtract(4, 2))
    print("Example: multiplication: ", calc.multiply(2, 3))
    print("Example: division: ", calc.divide(10, 2))
    print("Example: modulo: ", calc.modulo(10, 3))