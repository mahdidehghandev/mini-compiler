# import math

# def is_single_input_op(element):
#     ops = ['sin', 'cos', 'tan', 'cot', 'arcsin', 'arccos',
#            'arctan', 'arccot', 'log', 'sqrt', 'sqr', 'exp', 'unary-']
#     return element in ops


# def is_double_input_op(element):
#     ops = ['+', '-', 'mod', 'div', '*', '/', '^']
#     return element in ops



# def evaluate(arr):
#     nums_stack = []
#     print(f"Input postfix expression: {arr}")
    
#     for element in arr:
#         print(f"\nProcessing element: {element}")
#         print(f"Stack before operation: {nums_stack}")
        
#         if element.replace('.', '', 1).isdigit():  # Support for floats
#             nums_stack.append(float(element))
#         elif is_double_input_op(element):
#             if len(nums_stack) < 2:
#                 raise Exception(f"len of the stack is less than required for a double-input operation: {nums_stack}")
#             top_element = nums_stack.pop()
#             bottom_element = nums_stack.pop()

#             if element == '+':
#                 nums_stack.append(bottom_element + top_element)
#             elif element == '-':
#                 nums_stack.append(bottom_element - top_element)
#             elif element == '*':
#                 nums_stack.append(bottom_element * top_element)
#             elif element == '/':
#                 nums_stack.append(bottom_element / top_element)
#             elif element == '^':
#                 nums_stack.append(bottom_element ** top_element)
#             elif element == 'mod':
#                 nums_stack.append(bottom_element % top_element)
#             elif element == 'div':
#                 nums_stack.append(bottom_element // top_element)
#         elif is_single_input_op(element):
#             if len(nums_stack) < 1:
#                 raise Exception(f"len of the stack is less than required for a single-input operation: {nums_stack}")
#             top_element = nums_stack.pop()
#             if element == 'unary-':
#                 nums_stack.append((-top_element))
#             elif element == 'sin':
#                 nums_stack.append(math.sin(top_element))
#             elif element == 'cos':
#                 nums_stack.append(math.cos(top_element))
#             elif element == 'tan':
#                 nums_stack.append(math.tan(top_element))
#             elif element == 'cot':
#                 nums_stack.append(1 / math.tan(top_element))
#             elif element == 'arcsin':
#                 nums_stack.append(math.asin(top_element))
#             elif element == 'arccos':
#                 nums_stack.append(math.acos(top_element))
#             elif element == 'arctan':
#                 nums_stack.append(math.atan(top_element))
#             elif element == 'arccot':
#                 nums_stack.append(1 / math.atan(top_element))
#             elif element == 'log':
#                 nums_stack.append(math.log(top_element))
#             elif element == 'sqrt':
#                 nums_stack.append(math.sqrt(top_element))
#             elif element == 'sqr':
#                 nums_stack.append(top_element ** 2)
#             elif element == 'exp':
#                 nums_stack.append(math.exp(top_element))

#         else:
#             raise Exception(f"Invalid element: {element}")
        
#         print(f"Stack after operation: {nums_stack}")
    
#     if len(nums_stack) != 1:
#         raise Exception("The postfix expression is invalid. Remaining stack:", nums_stack)

#     return nums_stack.pop()



# # Example usage
# arr = ['5', '4', '*', '1', 'arctan', '*', '180', '/', 'sin', 'unary-', 'unary-']
# result = evaluate(arr)
# print("Result:", result)

def is_number(entry):

    if isinstance(entry, int):
        return True
    elif isinstance(entry, float):
        return True
    else:
        return False
print(is_number('5'))