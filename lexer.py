

class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __str__(self):
        return f'Token({self.type}, {repr(self.value)})'


class Lexer:
    def __init__(self, text):
        self.text = text
        self.line = 1
        self.beginning = 0
        self.forward = 0
        self.operators = ['+', '-', '*', '/', 'div', 'mod', '^', '(', ')']
        self.tokens = []
        

    def error(self):
        raise Exception(f"ERROR at line {self.line}, position {self.forward}: {self.text[self.forward]}")


    def create_token(self, type):
        lexeme = self.text[self.beginning:self.forward]
        token = Token(type=type, value=lexeme)
        self.tokens.append(token)
        return token
        
        
    def tokenize(self):
        while self.forward < len(self.text):
            char = self.text[self.forward]

            if char == '/' and self.forward + 1 < len(self.text) and self.text[self.forward + 1] == '/':
                self.is_single_line_comment()
            elif char in self.operators:
                self.is_operator()
            elif char.isdigit():  
                self.is_number()
            elif char.isalpha() or char == '_':  
                self.is_identifier()
            elif char.isspace():
                self.skip_white_space()
            else:  
                self.error()

        token = Token(type="EOF", value=None)
        self.tokens.append(token)
        return self.tokens


    def is_single_line_comment(self):
        
        self.forward += 2  
        while self.forward < len(self.text) and self.text[self.forward] != '\n':
            self.forward += 1
        self.beginning = self.forward  


    def is_multi_line_comment(self):
        self.forward += 1
        while self.forward < len(self.text):
            char = self.text[self.forward]
            if char == '}':
                self.forward += 1
                self.beginning = self.forward
                return
            if char == '\n': 
                self.line += 1
            self.forward += 1
        self.error() 


    def skip_white_space(self):
        while self.forward < len(self.text) and self.text[self.forward].isspace():
            if self.text[self.forward] == '\n':  
                self.line += 1
            self.forward += 1
        self.beginning = self.forward


    def is_number(self):
        state = 0
        while self.forward < len(self.text):
            char = self.text[self.forward]
            match (state):
                case 0:
                    if char.isdigit():
                        state = 1
                        self.forward += 1
                    
                case 1:
                    if char.isdigit():
                        state = 1
                        self.forward += 1
                        
                    elif char == '.':
                        state = 2
                        self.forward += 1
                        
                    elif char == 'e' or char == 'E':
                        state = 4
                        self.forward += 1
                    elif char.isalpha() or char == '_':
                        state = -1
                        
                    else:
                        state = 7
                        
                    
                case 2:
                    if char.isdigit():
                        state = 3
                    else:
                        state = -1
                    self.forward += 1
                        
                case 3:
                    if char.isdigit():
                        state = 3
                        self.forward += 1
                    elif char == 'e' or char == 'E':
                        state = 4
                        self.forward += 1

                    else:
                        state = 7
                        

                case 4:
                    if char.isdigit():
                        state = 6
                    elif char == '+' or char == '-':
                        state = 5
                    else:
                        state = -1
                    self.forward += 1
                        
                case 5:
                    if char.isdigit():
                        state = 6
                        self.forward += 1 
                    else:
                        state = -1
                case 6:
                    if char.isdigit():
                        state = 6
                        self.forward += 1
                    else:
                        state = 7
                        

                case 7:
                    self.create_token("NUM")
                    self.beginning = self.forward
                    return


                case -1:
                    raise Exception(
                        f"Invalid number format starting at position {self.beginning}"
                    )
                    
        if state in {1, 3, 6}:  
            self.create_token("NUM")
        else:
            self.error()    
            
                
    def is_identifier(self):
        state = 0
        while self.forward < len(self.text):
            char = self.text[self.forward]
            match state:
                case 0:
                    if char.isalpha() or char == '_':
                        state = 1
                        self.forward += 1
                case 1:
                    if char.isalpha() or char == '_' or char.isdigit():
                        state = 1
                        self.forward += 1
                    else:
                        state = 2
                
                case 2:
                    self.create_token("ID")
                    self.beginning = self.forward
                    return
 
 
    def is_operator(self):
        for op in self.operators:
            if self.text[self.forward:self.forward + len(op)] == op:
                self.forward += len(op)
                self.create_token("OPERATOR")
                self.beginning = self.forward
                return
        self.error()

            