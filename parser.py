class Parser:
    
    def __init__(self, tokens):
        self.tokens = tokens
        self.lookahead = tokens[0] if tokens else None 
        self.position = 0
        self.postfix = []
    
    def __str__(self):
        return (f"{self.postfix}\n")

    
    def get_next_token(self):
        self.position += 1
        if self.position < len(self.tokens):
            self.lookahead = self.tokens[self.position]
        else:
            self.lookahead = None  


    def match(self, char):
        if self.lookahead and self.lookahead.value == char:
            self.get_next_token()
        else:
            if self.lookahead:
                raise Exception(
                    f"Syntax error at Line {self.lookahead.line} "
                    f"Expected '{char}', got '{self.lookahead.value}'"
                )
            else:
                raise Exception("Syntax error: Unexpected end of input")
        
        
    def parse(self):
        self.expr()
        if self.lookahead.type == "EOF":
            print("PARSING SUCCESSFUL")
            
            
    def expr(self):
        self.term()
        self.expr_prime()
        
        
    def expr_prime(self):
        match self.lookahead.value:
            case '+':
                token = self.lookahead
                
                self.match('+')
                self.term() 
                self.postfix.append(token)
                self.expr_prime()
            case '-':
                token = self.lookahead
                
                self.match('-')
                self.term() 
                self.postfix.append(token)
                self.expr_prime()
            case _:
                return
        
        
    def term(self):
        self.power()
        self.term_prime()
        
        
    def term_prime(self):
        match self.lookahead.value:
            case '/':
                token = self.lookahead
                self.match('/')
                self.power()
                self.postfix.append(token)
                self.term_prime()
                
            case '*':
                token = self.lookahead
                
                self.match('*')
                self.power()
                self.postfix.append(token)
                self.term_prime()
                
            case 'mod':
                token = self.lookahead
                
                self.match('mod')

                if self.lookahead.type != "NUM" or '.' in self.lookahead.value:
                    raise Exception(f"Syntax error at Line {self.lookahead.line}: 'mod' requires an integer operand")
                
                self.power()
                self.postfix.append(token)
                self.term_prime()
                
            case 'div':    
                token = self.lookahead
                  
                self.match('div')
                self.power()
                self.postfix.append(token)
                self.term_prime()
            case _:
                return
          
                
    def power(self):
        self.factor()
        if self.lookahead.value == '^':
            token = self.lookahead
            self.match('^')
            self.power()
            self.postfix.append(token)


    def factor(self):
        if self.lookahead.value == '-':
            token = self.lookahead
            self.match('-')
            token.value = 'unary-'
            self.factor()  
            self.postfix.append(token)
            
        elif self.lookahead.type == "NUM":
            self.number()
            
        elif self.lookahead.value == '(':
            self.match('(')
            self.expr()
            self.match(')')
            
        elif self.lookahead.value.lower() in ['sin', 'cos', 'tan', 'cot', 'arcsin', 'arccos', 'arctan', 'arccot', 'log', 'sqrt', 'sqr', 'exp']:
            token = self.lookahead
            
            math_func = self.lookahead.value
            self.match(math_func)
            self.match('(')
            self.expr()
            self.match(')')
            self.postfix.append(token)
            
        elif self.lookahead.type == "ID":
            self.identifier()
        else:
            raise Exception(f"Syntax error at Line {self.lookahead.line} "
                            f"Unexpected factor '{self.lookahead.value}'")


    def number(self):
        self.digits()
        self.optional_fraction()
        self.optional_exponent()
    
    
    def digits(self):
        if self.lookahead.type == "NUM":
            token = self.lookahead
            
            digit = self.lookahead.value
            self.match(digit)
            self.postfix.append(token)
            self.digits_prime()
        

    def digits_prime(self):
        if self.lookahead.type == "NUM":  
            token = self.lookahead
            
            digit = self.lookahead.value
            self.match(digit)
            self.postfix.append(token) 
            self.digits_prime() 
        else:
            return
        
        
    def optional_fraction(self):
        if self.lookahead and self.lookahead.value == '.':  
            token = self.lookahead
            
            self.match('.')  
            self.digits()  
            self.postfix.append(token) 
    
    
    def optional_exponent(self):
        if self.lookahead.value == 'E':
            self.match('E') 

            if self.lookahead.value in ['+', '-']:  
                sign = self.lookahead.value
                self.match(sign)
            else:
                sign = ''  
            
            self.digits() 
        elif self.lookahead.value == 'e':
            self.match('e') 

            if self.lookahead.value in ['+', '-']:  
                sign = self.lookahead.value
                self.match(sign)

            else:
                sign = ''  
            
            self.digits() 
            

    def identifier(self):
        if self.lookahead.type == "ID": 
            token = self.lookahead
            self.postfix.append(token) 
            self.get_next_token()  
        else:
            raise Exception(f"Syntax error: Expected an identifier, got '{self.lookahead.value}'")


    
