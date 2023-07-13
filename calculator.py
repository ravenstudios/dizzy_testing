class Calculator:

    def add(self, *numbers):
        if self.validation(numbers[0]):
            result = 0
            for num in numbers:
                result += num
            return result

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        return a / b

    def validation(self, *query):
        for q in query:
            if type(q) != int and type(q) != float:
                raise Exception("Must use a type of int or float")
        return True
