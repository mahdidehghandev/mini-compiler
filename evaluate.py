import math


class Evaluate:
    def __init__(self, postfix_expr, symbol_table):
        self.postfix_expr = postfix_expr
        self.identifier_vals = {}
        self.symbol_table = symbol_table


    @staticmethod
    def convert_to_num(entry):
        try:
            num = float(entry)
            return int(num) if num.is_integer() else num
        except ValueError:
            raise Exception("ERROR: Invalid number format")

    


    @staticmethod
    def _apply_binary_op(op, a, b):
        if op == "+":
            return a + b
        elif op == "-":
            return a - b
        elif op == "*":
            return a * b
        elif op == "/":
            return a / b
        elif op == "^":
            return a**b
        elif op == "mod":
            if isinstance(b, float):  #! check if there is a float number after the mod
                raise Exception("Syntax error: 'mod' requires an integer operand")

            return a % b
        elif op == "div":
            return a // b
        else:
            raise Exception(f"Unknown binary operator: {op}")

    @staticmethod
    def _apply_single_op(op, a):
        if op == "unary-":
            return -a
        elif op == "sin":
            return math.sin(a)
        elif op == "cos":
            return math.cos(a)
        elif op == "tan":
            return math.tan(a)
        elif op == "cot":
            return 1 / math.tan(a)
        elif op == "arcsin":
            if -1 <= a <= 1:
                return math.asin(a)
            raise Exception("arcsin domain error")
        elif op == "arccos":
            if -1 <= a <= 1:
                return math.acos(a)
            raise Exception("arccos domain error")
        elif op == "arctan":
            return math.atan(a)
        elif op == "arccot":
            return 1 / math.atan(a)
        elif op == "log":
            if a > 0:
                return math.log(a)
            raise Exception("log domain error")
        elif op == "sqrt":
            if a >= 0:
                return math.sqrt(a)
            raise Exception("sqrt domain error")
        elif op == "sqr":
            return a**2
        elif op == "exp":
            return math.exp(a)
        else:
            raise Exception(f"Unknown unary operator: {op}")


    def get_values(self):
        for token in self.postfix_expr:
            print(token)
            if (token.type == "ID") and (
                self.symbol_table.table[token.value.lower()]["type"] == "IDENTIFIER"
                and self.symbol_table.table[token.value.lower()]["value"] is None
            ):
                value = input(f"Enter the value for '{token.value}': ")
                result = self.convert_to_num(value)
                self.symbol_table.table[token.value.lower()]["value"] = result



    def put_values(self, value):
        for token in self.postfix_expr:
            if (token.type == "ID") and not self.symbol_table.is_not_reserved(token.value.lower()) and not self.symbol_table.is_id_existence(token.value.lower()):
                self.symbol_table.add_id(token.value.lower())
                result = self.convert_to_num(value)
                self.symbol_table.table[token.value.lower()]["value"] = result



    def is_number(self, entry):
        entry = self.convert_to_num(entry)
        if isinstance(entry, int):
            return True

        elif isinstance(entry, float):
            return True

        else:
            return False

    
    def evaluate_expression(self):
        operand_stack = []

        for element in self.postfix_expr:
            if element.type == "ID" and self.symbol_table.is_id_existence:
                operand_stack.append(
                    self.symbol_table.table[element.value.lower()]["value"]
                )
            elif self.symbol_table.is_binary_op(element.value.lower()):
                if len(operand_stack) < 2:
                    raise Exception("Insufficient operands for binary operation.")
                top_element = operand_stack.pop()
                bottom_element = operand_stack.pop()
                operand_stack.append(
                    self._apply_binary_op(
                        element.value.lower(), bottom_element, top_element
                    )
                )

            elif self.symbol_table.is_single_op(element.value.lower()):
                if len(operand_stack) < 1:
                    raise Exception("Insufficient operands for binary operation.")
                top_element = operand_stack.pop()
                operand_stack.append(
                    self._apply_single_op(element.value.lower(), top_element)
                )

            elif self.is_number(element.value):
                operand_stack.append(self.convert_to_num(element.value))

            else:
                raise Exception(f"Invalid element: {element.value}")
        if len(operand_stack) != 1:
            raise Exception(
                "Invalid postfix expression. Stack contains:", operand_stack
            )
        return operand_stack.pop()

    def evaluate(self):
        self.get_values()
        return self.evaluate_expression()

    def evaluate_with_value(self, value):
        self.put_values(value)
        return self.evaluate_expression()
