class Parser:
    
    def __init__(self, tokens):
        self.tokens = tokens
        self.lookahead = tokens[0] if tokens else None 
        self.position = 0
        self.postfix = []
    
    def __str__(self):
        return (

        f"{self.postfix}\n"
        )

    
    def get_next_token(self):
        self.position += 1
        if self.position < len(self.tokens):
            self.lookahead = self.tokens[self.position]
        else:
            self.lookahead = None  

    def match(self, char):
        print(self.lookahead)
        if self.lookahead.value == char:
            self.get_next_token()
        else:
            raise Exception(f"Syntax error: expected '{char}', got '{self.lookahead}'")
        
        
        
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
                self.match('+')
                self.term() 

                self.postfix.append('+')
                self.expr_prime()
            case '-':
                self.match('-')
                self.term() 
                self.postfix.append('-')
                self.expr_prime()
            case _:
                return
        
    def term(self):
        self.power()
        self.term_prime()
        
    def term_prime(self):
        match self.lookahead.value:
            case '/':
                self.match('/')
                self.power()
                self.postfix.append('/')
                self.term_prime()
                
            case '*':
                self.match('*')
                self.power()
                self.postfix.append('*')
                self.term_prime()
                
            case 'mod':
                self.match('mod')
                self.power()
                self.postfix.append('mod')
                self.term_prime()
                
            case 'div':      
                self.match('div')
                self.power()
                self.postfix.append('div')
                self.term_prime()
            case _:
                return
                
    def power(self):
        self.factor()
        if self.lookahead.value == '^':
            self.match('^')
            self.power()
            self.postfix.append('^')

    def factor(self):
        if self.lookahead.value == '-':
            self.match('-')
            self.factor()  
            self.postfix.append('-')
        elif self.lookahead.type == "NUM":
            self.number()
        elif self.lookahead.value == '(':
            self.match('(')
            self.expr()
            self.match(')')
        elif self.lookahead.value.lower() in ['sin', 'cos', 'tan', 'cot', 'arcsin', 'arccos', 'arctan', 'arccot', 'log', 'sqrt', 'sqr', 'exp']:
            math_func = self.lookahead.value
            self.match(math_func)
            self.match('(')
            self.expr()
            self.match(')')
            self.postfix.append(math_func)
        elif self.lookahead.type == "ID":
            self.identifier()
        else:
            raise Exception(f"Syntax error: unexpected factor '{self.lookahead.value}'")


    def number(self):
        self.digits()
        self.optional_fraction()
        self.optional_exponent()
    
    def digits(self):
        if self.lookahead.type == "NUM":
            digit = self.lookahead.value
            self.match(digit)
            self.postfix.append(digit)
            self.digits_prime()
        

    def digits_prime(self):
        if self.lookahead.type == "NUM":  
            digit = self.lookahead.value
            self.match(digit)
            self.postfix.append(digit) 
            self.digits_prime() 
        else:
            return
        
    def optional_fraction(self):
        if self.lookahead and self.lookahead.value == '.':  # Check if lookahead is '.'
            self.match('.')  # Match '.'
            self.digits()  # Parse digits after '.'
            self.postfix.append('.')  # Append '.' to postfix
    
    def optional_exponent(self):
        if self.lookahead.value == 'E':
            self.match('E') 
            print('E') 


            if self.lookahead.value in ['+', '-']:  
                sign = self.lookahead.value
                self.match(sign)
                print(sign) 
            else:
                sign = ''  
            
            self.digits() 
        elif self.lookahead.value == 'e':
            self.match('e') 
            print('e') 


            if self.lookahead.value in ['+', '-']:  
                sign = self.lookahead.value
                self.match(sign)
                print(sign) 
            else:
                sign = ''  
            
            self.digits() 
            

    def identifier(self):
        if self.lookahead.type == "ID":  # Ensure it's an ID token
            print(f"Parsing identifier: {self.lookahead.value}")
            self.postfix.append(self.lookahead.value)  # Add identifier to postfix
            self.get_next_token()  # Move to the next token
        else:
            raise Exception(f"Syntax error: Expected an identifier, got '{self.lookahead.value}'")

            
            


     
            
    

    


            