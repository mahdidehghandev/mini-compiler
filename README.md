
# Mini-Compiler

A Python-based mini-compiler that performs lexical analysis, parsing, evaluation, root finding, and function visualization.

## Features

1. **Lexical Analysis**:
   - Tokenizes the input code and builds a symbol table for identifiers, numbers, and other elements.

2. **Parsing**:
   - Converts the input expression into postfix notation (Reverse Polish Notation).

3. **Evaluation**:
   - Evaluates the postfix expression to compute results.


4. **Root Finding**:
   - Implements the bisection method to find roots of single-variable mathematical expressions within a given interval.
   - The function must be continuous and have exactly one root in the specified interval for the method to work correctly.


5. **Function Visualization**:
   - Visualizes <b>single-variable mathematical</b> expressions within a given range using Matplotlib.
   - Provides a clear graphical representation of the function's behavior over the specified interval.



## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/mahdidehghandev/mini-compiler.git
   cd mini-compiler
   ```

2. Install required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Run the Compiler**:

   ```bash
   python main.py
   ```

2. **Input File**:
   - Place your input code in `input1.txt`. Example content:
   ```
      -(- sin (x  * 4*arctan(1) /180) //term1
            + log (exp(Y1))/log(e) {term2}+ sqrt(sqr(-_xY_2__z_))//term3
            {
                  comment
            }
            -2^2^3+X div 10-y1 mod  3+2.31+0.69+1.3E+2)
   ```
   - You can change the directory in   `main.py`
   ```python
   if __name__ == "__main__":
    main(os.path.join('Examples','test.txt')) # Change this section

   ```
3. **Menu Options**:
   - `1`: Evaluate the expression without visualization.
   - `2`: Visualize the function within a specified interval.
   - `3`: Find the root of the function using the bisection method.
   - `4`: Exit the program.

## Example

Given the input `y = x^3 - 2x + 1;`, you can:

- Compute the value of `y` for a specific `x`.
- Visualize the curve of `y` for a range of `x` values.
- Find the root of the equation in a given interval.

## Code Structure

- `main.py`: The entry point for the program.
- `lexer.py`: Handles tokenization and builds the symbol table.
- `parser.py`: Parses tokens and generates postfix expressions.
- `evaluate.py`: Evaluates the postfix expression.
- `symbol_table.py`: Manages the symbol table for variables and constants.

## Contribution

Feel free to fork the repository and submit pull requests for enhancements or bug fixes.


## Contributors

- [Mahdi Dehghan](https://github.com/mahdidehghandev) 
- [Ehsan Shafiei](https://github.com/Ehsanshafi3i)
##
<b>Adios amigos<br>
Happy coding!</b>

