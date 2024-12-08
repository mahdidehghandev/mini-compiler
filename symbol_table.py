class SymbolTable:
    #! variables , functions , 
    #* inside the lexical analyzer when it hits to a ID it creates an entry for it
    def __init__(self):
        self.table = {
            '+': {'type': 'OPERATOR', 'args': 2},
            '-': {'type': 'OPERATOR', 'args': 2},
            '*': {'type': 'OPERATOR', 'args': 2},
            '/': {'type': 'OPERATOR', 'args': 2},
            'div' : {'type': 'OPERATOR', 'args': 2},
            'mod' : {'type': 'OPERATOR', 'args': 2},
            '^': {'type': 'OPERATOR', 'args': 2},
            'unary-': {'type': 'OPERATOR','args': 1},
            '(': {'type': 'DELIMITER'},
            ')': {'type': 'DELIMITER'},
            'e': {'type': 'IDENTIFIER', 'value': 2.71},
            'sin': {'type': 'FUNCTION', 'args': 1},
            'cos': {'type': 'FUNCTION', 'args': 1},
            'tan': {'type': 'FUNCTION', 'args': 1},
            'cot': {'type': 'FUNCTION', 'args': 1},
            'arcsin': {'type': 'FUNCTION', 'args': 1},
            'arccos': {'type': 'FUNCTION', 'args': 1},
            'arctan': {'type': 'FUNCTION', 'args': 1},
            'arccot': {'type': 'FUNCTION', 'args': 1},
            'log': {'type': 'FUNCTION', 'args': 1},  
            'sqrt': {'type': 'FUNCTION', 'args': 1},
            'sqr': {'type': 'FUNCTION', 'args': 1},
            'exp': {'type': 'FUNCTION', 'args': 1},
            
        }

        
    
    