import math


class Evaluate:

    def __init__(self, postfix_expr):
        self.postfix_expr = postfix_expr
        self.identifier_vals = {}


    def get_values(self):
        for token in self.postfix_expr:
            if token.type == "ID" and token.value not in ['div', 'mod', 'sin', 'cos', 'tan', 'cot', 'arcsin', 'arccos', 'arctan', 'arccot', 'log', 'sqrt', 'sqr', 'exp']:
                token_lower = token.value.lower()

                if token_lower not in self.identifier_vals and token_lower != 'e':
                    value = input(f"Enter the value for '{token.value}': ")
                    result = self.convert_to_num(value)
                    self.identifier_vals[token_lower] = result
                elif token_lower == 'e':
                    value = 2.71
                    result = self.convert_to_num(value)
                    self.identifier_vals[token_lower] = result


    def put_values(self, value):
        for token in self.postfix_expr:
            if token.type == "ID" and token.value not in ['div', 'mod', 'sin', 'cos', 'tan', 'cot', 'arcsin', 'arccos', 'arctan', 'arccot', 'log', 'sqrt', 'sqr', 'exp']:
                token_lower = token.value.lower()

                if token_lower not in self.identifier_vals and token_lower != 'e':
                    result = self.convert_to_num(value)
                    self.identifier_vals[token_lower] = result
                elif token_lower == 'e':
                    value = 2.71
                    result = self.convert_to_num(value)
                    self.identifier_vals[token_lower] = result


    def is_number(self, entry):
        entry = self.convert_to_num(entry)
        if isinstance(entry, int):
            return True
        
        elif isinstance(entry, float):
            return True
        
        else:
            return False


    def convert_to_num(self, entry):
        try:
            num = float(entry)
            return int(num) if num.is_integer() else num
        except ValueError:
            raise Exception("ERROR: Invalid number format")


    def is_single_op(self, element):
        ops = ['sin', 'cos', 'tan', 'cot', 'arcsin', 'arccos',
               'arctan', 'arccot', 'log', 'sqrt', 'sqr', 'exp', 'unary-']
        return element in ops


    def is_binary_op(self, element):
        ops = ['+', '-', 'mod', 'div', '*', '/', '^']
        return element in ops


    def evaluate(self):
        self.get_values()
        operand_stack = []

        for element in self.postfix_expr:


            if element.type == "ID" and element.value not in ['div', 'mod', 'sin', 'cos', 'tan', 'cot', 'arcsin', 'arccos', 'arctan', 'arccot', 'log', 'sqrt', 'sqr', 'exp']:
                number = self.identifier_vals[f'{element.value.lower()}']
                operand_stack.append(number)
                
            elif self.is_binary_op(element.value):
                if len(operand_stack) < 2:
                    raise Exception(
                        f"len of the stack is less than required for a double-input operation: {operand_stack}")
                top_element = operand_stack.pop()
                bottom_element = operand_stack.pop()

                if element.value == '+':
                    operand_stack.append(bottom_element + top_element)

                elif element.value == '-':
                    operand_stack.append(bottom_element - top_element)

                elif element.value == '*':
                    operand_stack.append(bottom_element * top_element)

                elif element.value == '/':
                    operand_stack.append(bottom_element / top_element)

                elif element.value == '^':
                    operand_stack.append(bottom_element ** top_element)

                elif element.value == 'mod':
                    operand_stack.append(bottom_element % top_element)

                elif element.value == 'div':
                    operand_stack.append(bottom_element // top_element)

            elif self.is_single_op(element.value):
                if len(operand_stack) < 1:
                    raise Exception(
                        f"len of the stack is less than required for a single-input operation: {operand_stack}")
                top_element = operand_stack.pop()

                if element.value == 'unary-':
                    operand_stack.append((-top_element))

                elif element.value == 'sin':
                    operand_stack.append(math.sin(top_element))

                elif element.value == 'cos':
                    operand_stack.append(math.cos(top_element))

                elif element.value == 'tan':
                    operand_stack.append(math.tan(top_element))

                elif element.value == 'cot':
                    operand_stack.append(1 / math.tan(top_element))

                elif element.value == 'arcsin':
                    operand_stack.append(math.asin(top_element))

                elif element.value == 'arccos':
                    operand_stack.append(math.acos(top_element))

                elif element.value == 'arctan':
                    operand_stack.append(math.atan(top_element))

                elif element.value == 'arccot':
                    operand_stack.append(1 / math.atan(top_element))

                elif element.value == 'log':
                    operand_stack.append(math.log(top_element))

                elif element.value == 'sqrt':
                    operand_stack.append(math.sqrt(top_element))

                elif element.value == 'sqr':
                    operand_stack.append(top_element ** 2)

                elif element.value == 'exp':
                    operand_stack.append(math.exp(top_element))
                    
            elif self.is_number(element.value):
                number = self.convert_to_num(element.value)
                operand_stack.append(number)
                
            else:
                raise Exception(f"Invalid element: {element.value}")


        if len(operand_stack) != 1:
            raise Exception(
                "The postfix expression is invalid. Remaining stack:", operand_stack)

        return operand_stack.pop()


    def evaluate_with_value(self,value):
        self.put_values(value)
        operand_stack = []

        for element in self.postfix_expr:

            if element.type == "ID" and element.value not in ['div', 'mod', 'sin', 'cos', 'tan', 'cot', 'arcsin', 'arccos', 'arctan', 'arccot', 'log', 'sqrt', 'sqr', 'exp']:
                number = self.identifier_vals[f'{element.value.lower()}']
                operand_stack.append(number)
                
            elif self.is_binary_op(element.value):
                if len(operand_stack) < 2:
                    raise Exception(
                        f"len of the stack is less than required for a double-input operation: {operand_stack}")
                top_element = operand_stack.pop()
                bottom_element = operand_stack.pop()

                if element.value == '+':
                    operand_stack.append(bottom_element + top_element)

                elif element.value == '-':
                    operand_stack.append(bottom_element - top_element)

                elif element.value == '*':
                    operand_stack.append(bottom_element * top_element)

                elif element.value == '/':
                    operand_stack.append(bottom_element / top_element)

                elif element.value == '^':
                    operand_stack.append(bottom_element ** top_element)

                elif element.value == 'mod':
                    operand_stack.append(bottom_element % top_element)

                elif element.value == 'div':
                    operand_stack.append(bottom_element // top_element)

            elif self.is_single_op(element.value):
                if len(operand_stack) < 1:
                    raise Exception(
                        f"len of the stack is less than required for a single-input operation: {operand_stack}")
                top_element = operand_stack.pop()

                if element.value == 'unary-':
                    operand_stack.append((-top_element))

                elif element.value == 'sin':
                    operand_stack.append(math.sin(top_element))

                elif element.value == 'cos':
                    operand_stack.append(math.cos(top_element))

                elif element.value == 'tan':
                    operand_stack.append(math.tan(top_element))

                elif element.value == 'cot':
                    operand_stack.append(1 / math.tan(top_element))

                elif element.value == 'arcsin':
                    operand_stack.append(math.asin(top_element))

                elif element.value == 'arccos':
                    operand_stack.append(math.acos(top_element))

                elif element.value == 'arctan':
                    operand_stack.append(math.atan(top_element))

                elif element.value == 'arccot':
                    operand_stack.append(1 / math.atan(top_element))

                elif element.value == 'log':
                    operand_stack.append(math.log(top_element))

                elif element.value == 'sqrt':
                    operand_stack.append(math.sqrt(top_element))

                elif element.value == 'sqr':
                    operand_stack.append(top_element ** 2)

                elif element.value == 'exp':
                    operand_stack.append(math.exp(top_element))
                    
            elif self.is_number(element.value):
                number = self.convert_to_num(element.value)
                operand_stack.append(number)
                
            else:
                raise Exception(f"Invalid element: {element.value}")

        if len(operand_stack) != 1:
            raise Exception(
                "The postfix expression is invalid. Remaining stack:", operand_stack)

        return operand_stack.pop()
