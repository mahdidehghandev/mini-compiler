import math
class SymbolTable:

    # * inside the lexical analyzer when it hits to a ID it creates an entry for it
    def __init__(self):
        self.table = {
            '+': {'type': 'OPERATOR', 'args': 2, "is_reserved": None},
            '-': {'type': 'OPERATOR', 'args': 2, "is_reserved": None},
            '*': {'type': 'OPERATOR', 'args': 2, "is_reserved": None},
            '/': {'type': 'OPERATOR', 'args': 2, "is_reserved": None},
            'div': {'type': 'OPERATOR', 'args': 2, "is_reserved": True},
            'mod': {'type': 'OPERATOR', 'args': 2, "is_reserved": True},
            '^': {'type': 'OPERATOR', 'args': 2, "is_reserved": None},
            'unary-': {'type': 'OPERATOR', 'args': 1, "is_reserved": None},
            'unary+': {'type': 'OPERATOR', 'args': 1, "is_reserved": None},
            '(': {'type': 'DELIMITER', "is_reserved": None},
            ')': {'type': 'DELIMITER', "is_reserved": None},
            'e': {'type': 'IDENTIFIER', 'value': 2.71, "is_reserved": True},
            'pi': {'type': 'IDENTIFIER', 'value': math.pi, "is_reserved": True},
            'sin': {'type': 'FUNCTION', 'args': 1, "is_reserved": True},
            'cos': {'type': 'FUNCTION', 'args': 1, "is_reserved": True},
            'tan': {'type': 'FUNCTION', 'args': 1, "is_reserved": True},
            'cot': {'type': 'FUNCTION', 'args': 1, "is_reserved": True},
            'arcsin': {'type': 'FUNCTION', 'args': 1, "is_reserved": True},
            'arccos': {'type': 'FUNCTION', 'args': 1, "is_reserved": True},
            'arctan': {'type': 'FUNCTION', 'args': 1, "is_reserved": True},
            'arccot': {'type': 'FUNCTION', 'args': 1, "is_reserved": True},
            'log': {'type': 'FUNCTION', 'args': 1, "is_reserved": True},
            'sqrt': {'type': 'FUNCTION', 'args': 1, "is_reserved": True},
            'sqr': {'type': 'FUNCTION', 'args': 1, "is_reserved": True},
            'exp': {'type': 'FUNCTION', 'args': 1, "is_reserved": True},

        }

    def is_function(self, entry):

        if entry in self.table and self.table[entry]["type"] == "FUNCTION":
            return True
        return False

    def is_operator(self, entry):
        if entry in self.table and self.table[entry]["type"] in ["OPERATOR","DELIMITER"] :
            return True
        return False

    def is_not_reserved(self, entry):
        if entry in self.table and not self.table[entry]["is_reserved"]:
            return True
        return False

    def is_id_existence(self, entry):
        if entry in self.table and self.table[entry]["type"] == "IDENTIFIER":
            return True
        return False

    def add_id(self, entry):
        self.table[entry] = {"type": "IDENTIFIER", "value": None, "is_reserved": None}

    def is_reserved(self,entry):
        if entry in self.table and not self.table[entry]["is_reserved"]:
            return True
        return False
    
    def is_binary_op(self,entry):
        if entry in self.table and (self.table[entry]["type"] in ["FUNCTION","OPERATOR"] and self.table[entry]["args"] == 2 ):
            return True
        return False
    
    def is_single_op(self,entry):
        if entry in self.table and (self.table[entry]["type"] in ["FUNCTION","OPERATOR"] and self.table[entry]["args"] == 1 ):
            return True
        return False